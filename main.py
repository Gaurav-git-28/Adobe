import os
import json
import nltk

from datetime import datetime
from utils.pdf_parser import extract_pages_from_pdf
from utils.chunker import chunk_text
from utils.embedder import embed_texts
from utils.ranker import build_faiss_index, search_top_k
from utils.summarizer import summarize_text

def load_documents(input_dir):
    documents = []
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            filepath = os.path.join(input_dir, filename)
            documents.append({
                "filename": filename,
                "pages": extract_pages_from_pdf(filepath)
            })
    return documents

def analyze_documents(documents, persona, job, top_k=5):
    all_chunks, chunk_doc_map = [], []
    for doc in documents:
        chunks = chunk_text(doc["pages"])
        all_chunks.extend(chunks)
        chunk_doc_map.extend([doc["filename"]] * len(chunks))

    chunk_texts = [chunk["text"] for chunk in all_chunks]
    chunk_embeddings = embed_texts(chunk_texts)
    
    query_embedding = embed_texts([f"{persona}. Task: {job}"]).reshape(1, -1)
    index = build_faiss_index(chunk_embeddings)

    top_indices, _ = search_top_k(index, query_embedding, k=top_k)
    
    extracted_sections, sub_section_analysis = [], []
    for rank, idx in enumerate(top_indices):
        chunk = all_chunks[idx]
        extracted_sections.append({
            "document": chunk_doc_map[idx],
            "page_number": chunk["page_number"],
            "section_title": chunk["text"][:60].replace("\n", " "),
            "importance_rank": rank + 1
        })
        sub_section_analysis.append({
            "document": chunk_doc_map[idx],
            "refined_text": summarize_text(chunk["text"]),
            "page_number": chunk["page_number"]
        })
    
    return extracted_sections, sub_section_analysis

def main():
    input_dir = "input"
    output_path = "output/challenge1b_output.json"

    persona = "HR professional"
    job = "Create and manage fillable forms for onboarding and compliance."
    
    documents = load_documents(input_dir)
    extracted_sections, sub_sections = analyze_documents(documents, persona, job)

    output = {
        "metadata": {
            "input_documents": [doc["filename"] for doc in documents],
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.utcnow().isoformat() + "Z"
        },
        "extracted_sections": extracted_sections,
        "sub_section_analysis": sub_sections
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"[✔] Analysis complete. Output saved to {output_path}")

if __name__ == "__main__":
    main()
