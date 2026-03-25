import streamlit as st
from src.loader import load_pdfs
from src.rag_pipeline import create_rag_chain

st.set_page_config(page_title="Mayo Clinic RAG Chatbot", layout="centered")
st.title("Mayo Clinic RAG Chatbot")

# Load PDFs
pdf_folder = "data/medical_docs/"
try:
    docs = load_pdfs(pdf_folder)
    st.success(f"Loaded {len(docs)} PDF(s)")
except ValueError as e:
    st.error(str(e))
    st.stop()

# Create RAG chain
st.info("Initializing RAG chain...")
chain = create_rag_chain(docs)

# Chat interface
query = st.text_input("Ask a question:")
if query:
    with st.spinner("Fetching answer..."):
        response = chain.run(query)
    st.success("Answer:")
    st.write(response)