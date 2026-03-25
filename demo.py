# ================== 1. Imports ==================
import os
import re
import json
import subprocess
from typing import Dict, List, Any

import fitz  # PyMuPDF
import pandas as pd
from tqdm import tqdm
import torch

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.llms import Ollama
from langchain_core.documents import Document

# OCR optional dependencies
try:
    from pdf2image import convert_from_path
    import pytesseract
    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False
    print("Warning: OCR dependencies not installed. OCR will be disabled.")

# ================== 2. Configuration ==================
# Paths
PDF_DIR = "./data/papers/raw"                # Input PDFs
PROCESSED_DIR = "./data/papers/processed"    # Output JSON files
META_OUT = "./"                              # Metadata CSV output
FAISS_PATH = "./faiss_index"                 # FAISS index location

# Text processing
CHUNK_SIZE = 512
CHUNK_OVERLAP = 64
TOP_K = 3

# Models
EMBED_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "qwen2:7b"          # Must be available in Ollama

# QA
QUESTION_FILE = "./evaluation/benchmarking_question.xlsx"
OUTPUT_FILE = "./rag_benchmark_output.csv"
MAX_QUESTIONS = 5            # Set to int to limit, None for all

# OCR (enable if needed)
USE_OCR = False

# ================== 3. PDF Preprocessing Functions ==================
def extract_metadata_from_filename(filename: str) -> Dict[str, str]:
    """Parse filename: FirstAuthor_Year_Title.pdf (flexible)."""
    base = os.path.splitext(filename)[0]
    parts = base.split('_')
    if len(parts) >= 2:
        author = parts[0]
        year = parts[1] if parts[1].isdigit() else ""
        title = ' '.join(parts[2:]) if len(parts) > 2 else ""
    else:
        author, year, title = "", "", base
    return {
        "file_name": filename,
        "authors": author,
        "year": year,
        "title": title
    }

def extract_text_with_pymupdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    text = "\n".join(page.get_text() for page in doc)
    doc.close()
    return text

def extract_text_with_ocr(pdf_path: str) -> str:
    if not OCR_AVAILABLE:
        raise RuntimeError("OCR not available.")
    images = convert_from_path(pdf_path)
    text = "\n".join(pytesseract.image_to_string(img, lang='eng') for img in images)
    return text

def clean_text(text: str) -> str:
    # Remove coordinates like text[[...]]
    text = re.sub(r'text\[\[.*?\]\]', '', text, flags=re.DOTALL)
    # Fix hyphenated line breaks
    text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)
    # Replace single newlines with space
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    # Collapse multiple spaces
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()

def process_pdf(pdf_path: str, use_ocr: bool = False) -> Dict[str, Any]:
    text = extract_text_with_pymupdf(pdf_path)
    if use_ocr and len(text.strip()) < 200:
        print(f"  Text too short ({len(text)} chars), trying OCR...")
        try:
            text = extract_text_with_ocr(pdf_path)
        except Exception as e:
            print(f"  OCR failed: {e}")

    doc = fitz.open(pdf_path)
    meta = doc.metadata
    doc.close()
    return {"text": text, "pdf_metadata": meta}

def preprocess_pdfs(pdf_dir: str, out_dir: str, meta_out: str, use_ocr: bool) -> List[Dict]:
    os.makedirs(out_dir, exist_ok=True)
    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print(f"No PDFs found in {pdf_dir}")
        return []

    records = []
    for pdf_file in tqdm(pdf_files, desc="Processing PDFs"):
        pdf_path = os.path.join(pdf_dir, pdf_file)
        try:
            file_meta = extract_metadata_from_filename(pdf_file)
            extracted = process_pdf(pdf_path, use_ocr)
            pdf_meta = extracted["pdf_metadata"]
            raw_text = extracted["text"]
            cleaned = clean_text(raw_text)

            title = pdf_meta.get("title", "").strip() or file_meta["title"]
            authors = pdf_meta.get("author", "").strip() or file_meta["authors"]
            year = file_meta["year"]

            record = {
                "file_id": os.path.splitext(pdf_file)[0],
                "file_name": pdf_file,
                "title": title,
                "authors": authors,
                "year": year,
                "source": pdf_meta.get("source", ""),
                "abstract": "",
                "keywords": "",
                "text": cleaned
            }

            json_path = os.path.join(out_dir, f"{record['file_id']}.json")
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(record, f, ensure_ascii=False, indent=2)

            meta_row = record.copy()
            meta_row.pop("text")
            meta_row["path_to_text"] = os.path.relpath(json_path, start=os.path.dirname(meta_out) or '.')
            records.append(meta_row)

        except Exception as e:
            print(f"\nError processing {pdf_file}: {e}")

    if records:
        df = pd.DataFrame(records)
        cols = ["file_name", "title", "authors", "year", "source", "abstract", "keywords", "path_to_text"]
        for col in cols:
            if col not in df.columns:
                df[col] = ""
        df = df[cols]
        csv_path = os.path.join(meta_out, "paper_metadata.csv")
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        print(f"\nMetadata saved to {csv_path}")
        print(f"Processed {len(records)} PDFs")
    return records

# ================== 4. RAG Pipeline Functions ==================
def load_processed_texts(processed_dir: str) -> List[Document]:
    json_files = [f for f in os.listdir(processed_dir) if f.endswith('.json')]
    docs = []
    for fname in json_files:
        with open(os.path.join(processed_dir, fname), 'r', encoding='utf-8') as f:
            data = json.load(f)
        doc = Document(
            page_content=data['text'],
            metadata={
                'source': data['file_name'],
                'title': data['title'],
                'authors': data['authors'],
                'year': data['year']
            }
        )
        docs.append(doc)
    print(f"Loaded {len(docs)} documents from {processed_dir}")
    return docs

def chunk_documents(docs: List[Document], chunk_size: int, chunk_overlap: int) -> List[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", "。", "！", "？", "；", "，", " ", ""]
    )
    chunks = splitter.split_documents(docs)
    print(f"Created {len(chunks)} chunks")
    return chunks

def build_faiss_index(chunks: List[Document], embed_model: str, faiss_path: str):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    emb = HuggingFaceEmbeddings(model_name=embed_model, model_kwargs={"device": device})
    db = FAISS.from_documents(chunks, emb)
    db.save_local(faiss_path)
    print(f"FAISS index saved to {faiss_path}")
    return db

def load_faiss_index(faiss_path: str, embed_model: str):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    emb = HuggingFaceEmbeddings(model_name=embed_model, model_kwargs={"device": device})
    db = FAISS.load_local(faiss_path, emb, allow_dangerous_deserialization=True)
    print(f"FAISS index loaded from {faiss_path}")
    return db

def check_ollama_model(model_name: str) -> bool:
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
        if model_name in result.stdout:
            return True
        else:
            print(f"Model '{model_name}' not found. Run: ollama pull {model_name}")
            return False
    except FileNotFoundError:
        print("Ollama not installed or not running.")
        return False

def build_rag_chain(retriever, llm_model: str):
    prompt = ChatPromptTemplate.from_template("""Answer the question based only on the context:
Context: {context}
Question: {question}
Answer:""")
    llm = Ollama(model=llm_model, temperature=0.3, num_predict=150)
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain

def run_batch_evaluation(retriever, rag_chain, question_file: str, output_file: str, max_questions=None):
    if not os.path.exists(question_file):
        print(f"Question file not found: {question_file}")
        return

    df_questions = pd.read_excel(question_file)
    if max_questions:
        df_questions = df_questions.head(max_questions)

    results = []
    for _, row in tqdm(df_questions.iterrows(), total=len(df_questions), desc="Running batch QA"):
        qid = row['QID']
        question = row['Question']
        target = row.get('Source Doc IDs', '')

        retrieved_docs = retriever.invoke(question)
        contexts = []
        sources = []
        for i, doc in enumerate(retrieved_docs):
            src = doc.metadata.get('source', 'Unknown')
            contexts.append(f"[Chunk {i+1} | Source: {src}]\n{doc.page_content}")
            sources.append(src)
        full_context = "\n\n------------------------\n\n".join(contexts)

        try:
            answer = rag_chain.invoke(question)
            answer_text = answer if isinstance(answer, str) else str(answer)
        except Exception as e:
            answer_text = f"Generation error: {e}"

        results.append({
            "QID": qid,
            "Question": question,
            "Target_Doc_IDs": target,
            "Generated_Answer": answer_text,
            "Retrieved_Context": full_context,
            "Retrieved_Sources": json.dumps(sources)
        })

    df_results = pd.DataFrame(results)
    df_results.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"\nResults saved to {output_file}")

# ================== 5. Main Execution ==================
def main():
    # Step 0: Check Ollama
    if not check_ollama_model(LLM_MODEL):
        return

    # Step 1: Preprocess PDFs (if needed)
    print("\n=== Step 1: PDF Preprocessing ===")
    if not os.path.exists(PROCESSED_DIR) or len(os.listdir(PROCESSED_DIR)) == 0:
        if not os.path.exists(PDF_DIR):
            print(f"PDF directory {PDF_DIR} does not exist.")
            return
        preprocess_pdfs(PDF_DIR, PROCESSED_DIR, META_OUT, USE_OCR)
    else:
        print(f"Processed texts already exist in {PROCESSED_DIR}. Skipping preprocessing.")

    # Step 2: Load and chunk documents
    print("\n=== Step 2: Load and Chunk Documents ===")
    docs = load_processed_texts(PROCESSED_DIR)
    if not docs:
        print("No documents loaded.")
        return
    chunks = chunk_documents(docs, CHUNK_SIZE, CHUNK_OVERLAP)

    # Step 3: Build or load FAISS index
    print("\n=== Step 3: FAISS Index ===")
    if os.path.exists(FAISS_PATH):
        db = load_faiss_index(FAISS_PATH, EMBED_MODEL)
    else:
        db = build_faiss_index(chunks, EMBED_MODEL, FAISS_PATH)
    retriever = db.as_retriever(search_kwargs={"k": TOP_K})

    # Step 4: Build RAG chain
    print("\n=== Step 4: Build RAG Chain ===")
    rag_chain = build_rag_chain(retriever, LLM_MODEL)

    # Step 5: Batch evaluation
    print("\n=== Step 5: Batch QA ===")
    run_batch_evaluation(retriever, rag_chain, QUESTION_FILE, OUTPUT_FILE, MAX_QUESTIONS)

    print("\nAll steps completed.")

def get_available_ollama_models():
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
        lines = result.stdout.strip().split('\n')[1:]
        return [line.split()[0] for line in lines if line]
    except: return []

# 核心：将 pipeline 步骤包装成可被 app.py 调用的函数
def run_preprocess(pdf_dir, processed_dir, meta_out, use_ocr):
    return preprocess_pdfs(pdf_dir, processed_dir, meta_out, use_ocr)

def initialize_rag(processed_dir, embed_model, faiss_path, chunk_size, chunk_overlap, top_k, llm_model):
    docs = load_processed_texts(processed_dir)
    chunks = chunk_documents(docs, chunk_size, chunk_overlap)
    if os.path.exists(faiss_path):
        db = load_faiss_index(faiss_path, embed_model)
    else:
        db = build_faiss_index(chunks, embed_model, faiss_path)
    retriever = db.as_retriever(search_kwargs={"k": top_k})
    chain = build_rag_chain(retriever, llm_model)
    return retriever, chain

if __name__ == "__main__":
    main()