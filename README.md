# RAG Medical Chatbot
# MediAssist AI – Intelligent Healthcare RAG Chatbot
An AI-powered healthcare chatbot that uses Retrieval-Augmented Generation (RAG) to provide reliable medical information from trusted medical datasets.

## Overview
MediAssist AI is a Generative AI healthcare chatbot designed to provide reliable medical information by retrieving knowledge from trusted healthcare sources and combining it with Large Language Models.The system uses a Retrieval-Augmented Generation (RAG) architecture to ensure responses are grounded in medical knowledge rather than relying purely on LLM memory.
This project demonstrates modern AI system design including data ingestion, vector embeddings, knowledge retrieval, and conversational AI interfaces.

## Features
• AI-powered healthcare question answering  
• Retrieval Augmented Generation (RAG) pipeline  
• Medical knowledge ingestion from trusted sources  
• Vector similarity search using embeddings   
• Interactive chatbot interface using Streamlit  

## Tech Stack
### Backend
- Python
- LangChain
### AI / ML
- OpenAI / LLM models
- Embeddings
- Retrieval Augmented Generation (RAG)
### Frontend
- Streamlit

## System Architecture
User Question -> Streamlit UI ->  Retriever (Vector Database) -> Medical Knowledge Sources -> Large Language Model -> AI Generated Response


## Setup
1. Clone the repository -> git clone https://github.com/gomathinagiri/rag-medical-chatbot.git ->  cd rag-medical-chatbot
2. Create virtual environment  ->  python -m venv venv
3. Activate environment ->  source venv/bin/activate
4. Add your PDFs into -> data/medical_docs/
5. Install dependencies -> pip install -r requirements.txt
