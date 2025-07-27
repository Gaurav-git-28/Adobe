import nltk
import pickle

# Define a basic chunk grammar (you can modify as needed)
grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>}   # Noun Phrase
    VP: {<VB.*><NP|PP|CLAUSE>+$}  # Verb Phrase
"""

# Create a RegexpParser chunker
chunker = nltk.RegexpParser(grammar)

# Save it as a pickle file
with open("english.pickle", "wb") as f:
    pickle.dump(chunker, f)

print("english.pickle has been created successfully.")
