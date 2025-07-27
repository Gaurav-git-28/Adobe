# utils/summarizer.py
import os
import pickle
from nltk.tokenize.punkt import PunktSentenceTokenizer

# Load tokenizer manually from downloaded file
punkt_path = r"C:\Users\admin\nltk_data\tokenizers\punkt\english.pickle"

with open(punkt_path, "rb") as f:
    tokenizer = pickle.load(f)

def sent_tokenize(text):
    return tokenizer.tokenize(text)


def summarize_text(text, max_sentences=2):
    sentences = sent_tokenize(text)
    return " ".join(sentences[:max_sentences])
