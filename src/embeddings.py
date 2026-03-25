from sentence_transformers import SentenceTransformer

def get_embeddings_model(model_name="all-MiniLM-L6-v2"):
    """
    Load SentenceTransformer model.
    """
    model = SentenceTransformer(model_name)
    return model

def embed_texts(docs, model):
    """
    Convert list of doc texts to embeddings.
    """
    embeddings = model.encode([doc["text"] for doc in docs], show_progress_bar=True)
    return embeddings
