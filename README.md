# RAG Medical Chatbot

## Setup

1. Add your PDFs into:
   data/medical_docs/

2. Install dependencies:
   pip install -r requirements.txt

3. Set OpenAI API key:
   export OPENAI_API_KEY=your_key_here

4. Run app:
   uvicorn app:app --reload

5. Open browser:
   http://127.0.0.1:8000/chat?query=What are symptoms of diabetes?
