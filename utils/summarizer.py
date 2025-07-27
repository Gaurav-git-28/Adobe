import nltk
from nltk.tokenize import sent_tokenize

# Ensure 'punkt' is available
nltk.download('punkt', quiet=True)

def split_into_sentences(text):
    return sent_tokenize(text)

def summarize_text(text, max_sentences=3):
    sentences = split_into_sentences(text)
    if len(sentences) <= max_sentences:
        return text
    else:
        return ' '.join(sentences[:max_sentences])
