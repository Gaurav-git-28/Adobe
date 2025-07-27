# utils/embedder.py
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")  # CPU-friendly, <100MB

def embed_texts(texts):
    return model.encode(texts, show_progress_bar=False, convert_to_numpy=True)
