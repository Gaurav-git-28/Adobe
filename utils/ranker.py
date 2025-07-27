# utils/ranker.py
import faiss
import numpy as np

def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def search_top_k(index, query_embedding, k=5):
    distances, indices = index.search(query_embedding, k)
    return indices[0], distances[0]
