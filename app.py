import streamlit as st
from rag_utils import read_pdf, split_text, smart_answer
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import time

# Configure Streamlit page
st.set_page_config(page_title="📄 Resume AI Chatbot", page_icon="🤖")

# Load models
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Session state variables
if "user_name" not in st.session_state:
    st.session_state.user_name = None

if "resume_uploaded" not in st.session_state:
    st.session_state.resume_uploaded = False

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if "chunk_embeddings" not in st.session_state:
    st.session_state.chunk_embeddings = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "text_data" not in st.session_state:
    st.session_state.text_data = ""

# --- Step 1: Welcome UI ---
st.markdown(
    "<h1 style='text-align: center; color: #4B8BBE;'>Get the complete information for uploaded Resume </h1>"
    "<p style='text-align: center;'>RAG-based smart assistant to help you to know about Candidate </p>",
    unsafe_allow_html=True
)

# Ask name if not already set
if st.session_state.user_name is None:
    name = st.text_input("👤 Enter your name to begin:")
    if name:
        st.session_state.user_name = name
        st.rerun()

# Step 2: Upload resume
if st.session_state.user_name:
    st.success(f"Welcome, {st.session_state.user_name}! Upload your resume to begin.")

    uploaded_file = st.file_uploader("📎 Upload your resume (PDF only, max 10MB)", type=["pdf"])

    if uploaded_file and not st.session_state.resume_uploaded:
        if uploaded_file.type != "application/pdf" or uploaded_file.size > 10 * 1024 * 1024:
            st.error("❌ Invalid file. Please upload a valid PDF under 10MB.")
        else:
            with st.spinner("📖 Analyzing your resume..."):
                text = read_pdf(uploaded_file)
                chunks = split_text(text)
                chunk_embeddings = embed_model.encode(chunks, convert_to_tensor=True)

                # Save to session
                st.session_state.chunks = chunks
                st.session_state.chunk_embeddings = chunk_embeddings
                st.session_state.resume_uploaded = True
                st.session_state.text_data = text
                time.sleep(1.5)

            st.success("✅ Resume analyzed successfully!")

# Step 3: Chat interface
if st.session_state.resume_uploaded:
    st.markdown("---")
    st.markdown("#### 💡 Ask any question about your resume (e.g., What are my cloud skills?)")

    # Chat input box
    user_query = st.chat_input("Ask a question...")

    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})

        with st.spinner("🤖 Thinking..."):
            # First try smart rule-based answer
            smart = smart_answer(user_query, st.session_state.text_data)
            if smart:
                response = smart
            else:
                # Fallback to QA
                query_embedding = embed_model.encode(user_query, convert_to_tensor=True)
                scores = util.cos_sim(query_embedding, st.session_state.chunk_embeddings)[0]
                top_k = min(3, len(st.session_state.chunks))
                top_results = scores.topk(k=top_k)
                top_chunks = [st.session_state.chunks[i] for i in top_results[1]]
                context_text = "\n".join(top_chunks)

                answer = qa_pipeline(question=user_query, context=context_text)
                response = answer["answer"]

                if response.strip() == "":
                    response = "🤖 Sorry, I couldn't find a confident answer. Try rephrasing your question."

        st.session_state.messages.append({"role": "assistant", "content": response})

    # Show chat history
    for msg in st.session_state.messages:
        with st.chat_message("user" if msg["role"] == "user" else "assistant"):
            st.markdown(msg["content"])
