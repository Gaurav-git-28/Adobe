import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag, ne_chunk

def chunk_text(text):
    sentences = sent_tokenize(text)  # Correct tokenizer
    chunks = []
    for sentence in sentences:
        tokens = word_tokenize(sentence)
        tagged = pos_tag(tokens)
        tree = ne_chunk(tagged)
        chunks.append(tree)
    return chunks
