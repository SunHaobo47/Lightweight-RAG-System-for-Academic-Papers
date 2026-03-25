## Run Configuration 

- Corpus path: `data/papers/raw/`
- File type: PDF only
- PDF loader: `PyPDFLoader`
- Chunking method: `RecursiveCharacterTextSplitter`
- Chunk size: `512`
- Chunk overlap: `64`
- Embedding model: `all-MiniLM-L6-v2`
- Vector store: `FAISS`
- Retrieval top-k: `3`
- Generator backend: `Ollama`
- Generator model: `qwen2:7b`
- Generation temperature: `0.1`
- QA prompt:
  `Answer the question based only on the context:
   Context: {context}
   Question: {question}
   Answer:`
- Question file: `evaluation/benchmarking_question.xlsx`
- Output file: `rag_benchmark_output.csv`
