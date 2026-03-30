from sentence_transformers import SentenceTransformer

def get_embeddings_model(model_name="all-MiniLM-L6-v2"):
    return SentenceTransformer(model_name)

def embed_texts(texts, model):
    return model.encode(texts, show_progress_bar=True)