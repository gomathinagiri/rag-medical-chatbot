from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain.chains.retrieval_qa.base import RetrievalQA
from transformers import pipeline

def create_rag_chain(docs, llm_model_name="google/flan-t5-base"):
    

    # ✅ Convert to Documents
    documents = [
        Document(page_content=doc["text"], metadata={"source": doc["filename"]})
        for doc in docs
    ]

    # ✅ Chunking (VERY IMPORTANT)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    split_docs = splitter.split_documents(documents)

    # ✅ Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # ✅ Vector DB
    vectorstore = FAISS.from_documents(split_docs, embeddings)

    # ✅ LLM (Better config)
    pipe = pipeline(
    "text-generation",
    model=llm_model_name,
    max_new_tokens=256,
    temperature=0.3
)
   

    llm = HuggingFacePipeline(pipeline=pipe)

    # ✅ Prompt
    prompt = PromptTemplate(
        template="""
You are a medical assistant AI.

Answer ONLY from the provided context.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
""",
        input_variables=["context", "question"]
    )

    # ✅ Chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": prompt}
    )

    return qa_chain