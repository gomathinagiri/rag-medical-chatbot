import streamlit as st
from src.loader import load_pdfs
from src.rag_pipeline import create_rag_chain

st.set_page_config(page_title="Medical RAG Chatbot", layout="centered")
st.title("Medical RAG Chatbot")

@st.cache_resource
def load_chain():
    docs = load_pdfs("data/medical_docs/")
    return create_rag_chain(docs)

try:
    chain = load_chain()
    st.success("RAG system ready ")
except Exception as e:
    st.error(str(e))
    st.stop()

query = st.text_input("Ask your medical question:")

if query:
    with st.spinner("Thinking..."):
        result = chain.invoke({"query": query})
        st.write(result["result"])