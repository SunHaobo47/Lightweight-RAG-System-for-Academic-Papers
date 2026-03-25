import streamlit as st
import pandas as pd
import os, time, json
import backend as sdk

# ================== 1. Page Configuration & State ==================
st.set_page_config(page_title="Lightweight RAG System for Academic Paper", layout="wide", page_icon="🔬")

# Initialize Session State
if "retriever" not in st.session_state: st.session_state.retriever = None
if "rag_chain" not in st.session_state: st.session_state.rag_chain = None
if "messages" not in st.session_state: st.session_state.messages = []

# ================== 2. Sidebar: Configuration & Monitoring ==================
with st.sidebar:
    st.header("⚙️ Global Configuration Panel")

    # System Status Monitoring
    st.subheader("🖥️ System Status")
    available_models = sdk.get_available_ollama_models()
    if available_models:
        st.success(f"Ollama Online ({len(available_models)} models)")
        llm_model = st.selectbox("LLM Model", available_models, index=0)
    else:
        st.error("Ollama service not detected")
        llm_model = "qwen2:7b"

    st.divider()
    st.subheader("📏 Chunking & Retrieval Parameters")
    chunk_size = st.slider("Chunk Size", 256, 1024, 512)
    chunk_overlap = st.slider("Chunk Overlap", 0, 128, 64)
    top_k = st.number_input("Top-K (Retrieved Chunks)", 1, 10, 3)
    embed_model = st.text_input("Embedding Model", "all-MiniLM-L6-v2")
    use_ocr = st.checkbox("Enable OCR Recognition", value=False)

# ================== 3. Main Interface Layout ==================
st.title("📚 Lightweight RAG System for Academic Paper")

tab_manage, tab_chat, tab_eval = st.tabs(["🗂️ Knowledge Base Management", "💬 Interactive Q&A (Citation)", "📊 Batch Evaluation Dashboard"])

# --- Tab 1: Knowledge Base Construction (Visual Progress Monitoring) ---
with tab_manage:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 1. Import PDF Resources")
        st.info(f"Reading Path: `{sdk.PDF_DIR}`")
        if st.button("🚀 Start Backend Preprocessing (PDF -> JSON)", use_container_width=True):
            with st.status("Processing PDFs...", expanded=True) as status:
                st.write("Calling backend `preprocess_pdfs` function...")
                sdk.run_preprocess(sdk.PDF_DIR, sdk.PROCESSED_DIR, sdk.META_OUT, use_ocr)
                status.update(label="Processing Complete! JSON files generated.", state="complete")

    with col2:
        st.markdown("### 2. Build/Load Index")
        if st.button("🧠 Initialize RAG Engine", type="primary", use_container_width=True):
            with st.spinner("Loading vector database and building chain..."):
                retriever, chain = sdk.initialize_rag(
                    sdk.PROCESSED_DIR, embed_model, sdk.FAISS_PATH,
                    chunk_size, chunk_overlap, top_k, llm_model
                )
                st.session_state.retriever = retriever
                st.session_state.rag_chain = chain
                st.success("RAG Engine Ready!")

# --- Tab 2: Interactive Q&A (Chat UI + Ground Truth) ---
with tab_chat:
    if st.session_state.rag_chain is None:
        st.warning("Please initialize the engine in 'Knowledge Base Management' first.")
    else:
        # --- New: Example Questions Section ---
        st.markdown("##### 💡 Example Questions (Click to ask directly)")
        # You can modify these questions based on your paper content
        example_questions = [
            "In the French-to-English translation setting, what common prompting failure mode do the authors observe?",
            "According to the paper, why is APE considered an automatic prompt engineering method?",
            "According to the paper, how is worst prompt performance defined?",
            "According to the paper, what problem does Repo-Level Prompt Generator (RLPG) solve, and what is its core value?"
        ]

        # Horizontal button layout using columns
        cols = st.columns(len(example_questions))
        clicked_question = None

        for i, q in enumerate(example_questions):
            if cols[i].button(q, use_container_width=True):
                clicked_question = q

        st.divider()

        # Render chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if "source" in message:
                    with st.expander("🔍 View Retrieval Citations (Ground Truth)"):
                        st.info(message["source"])

        # --- Core Logic ---
        # Get input: either from chat box or clicked example
        prompt = st.chat_input("Ask questions based on the paper content...")
        if clicked_question:
            prompt = clicked_question

        if prompt:
            # Add user message to history and display
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                # 1. Get citation information (Ground Truth)
                with st.spinner("Retrieving knowledge base..."):
                    docs = st.session_state.retriever.invoke(prompt)
                    source_text = "\n\n---\n\n".join([f"**Source: {d.metadata.get('source', 'Unknown')}**\n{d.page_content}" for d in docs])

                # 2. Generate response from LLM
                with st.spinner("Generating answer..."):
                    try:
                        response = st.session_state.rag_chain.invoke(prompt)
                        st.markdown(response)
                        with st.expander("🔍 View Retrieval Citations (Ground Truth)"):
                            st.info(source_text)

                        # Save assistant response to history
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": response,
                            "source": source_text
                        })
                    except Exception as e:
                        st.error(f"Error generating response: {e}")

            # Rerun to clear clicked state after example question
            if clicked_question:
                st.rerun()

# --- Tab 3: Batch Evaluation (Dashboard + Download) ---
with tab_eval:
    st.markdown("### 📈 Batch QA Evaluation Workflow")
    if st.button("🏃 Run Batch Evaluation Task", use_container_width=True):
        if st.session_state.rag_chain:
            with st.status("Running Batch QA...", expanded=True) as status:
                st.write("Reading Excel test dataset...")
                # Call backend batch evaluation function
                sdk.run_batch_evaluation(
                    st.session_state.retriever,
                    st.session_state.rag_chain,
                    sdk.QUESTION_FILE,
                    sdk.OUTPUT_FILE
                )
                status.update(label="Evaluation Complete!", state="complete")

            # Display results dashboard
            st.subheader("📋 Results Preview")
            df_res = pd.read_csv(sdk.OUTPUT_FILE)
            st.dataframe(df_res, use_container_width=True)

            # One-click download
            with open(sdk.OUTPUT_FILE, "rb") as f:
                st.download_button(
                    label="📥 Download CSV Evaluation Report",
                    data=f,
                    file_name="rag_report.csv",
                    mime="text/csv"
                )
        else:
            st.error("Please initialize the engine first.")