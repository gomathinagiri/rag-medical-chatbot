from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

def create_rag_chain(docs, embedding_model_name="all-MiniLM-L6-v2", llm_model_name="google/flan-t5-small"):
    # Convert docs to LangChain Documents
    lc_docs = [Document(page_content=doc["text"], metadata={"source": doc["filename"]}) for doc in docs]

    # Embeddings
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)

    # Create FAISS vectorstore
    vectorstore = FAISS.from_documents(lc_docs, embeddings)

    # LLM pipeline
    pipe = pipeline(
        "text2text-generation",
        model=llm_model_name,
        tokenizer=llm_model_name,
        max_length=512
    )
    llm = HuggingFacePipeline(pipeline=pipe)

    # Prompt template
    template = """Answer the question based on the context below.
Context: {context}
Question: {question}
Answer:"""
    prompt = PromptTemplate(template=template, input_variables=["context", "question"])

    # RetrievalQA chain
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )
    return chain