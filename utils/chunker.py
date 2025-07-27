import os
import pickle
from nltk.tokenize.punkt import PunktSentenceTokenizer

# Manually load the sentence model
punkt_path = r"C:\Users\admin\nltk_data\tokenizers\punkt\english.pickle"

if not os.path.exists(punkt_path):
    raise FileNotFoundError("english.pickle not found. Please ensure it's placed at the correct path.")

with open(punkt_path, "rb") as f:
    tokenizer = pickle.load(f)

def sent_tokenize(text):
    return tokenizer.tokenize(text)


def chunk_text(pages, max_words=200):
    chunks = []
    for page in pages:
        sentences = sent_tokenize(page["text"])
        chunk, word_count = "", 0
        for sent in sentences:
            words = sent.split()
            if word_count + len(words) > max_words:
                chunks.append({
                    "page_number": page["page_number"],
                    "text": chunk.strip()
                })
                chunk, word_count = "", 0
            chunk += " " + sent
            word_count += len(words)
        if chunk:
            chunks.append({
                "page_number": page["page_number"],
                "text": chunk.strip()
            })
    return chunks