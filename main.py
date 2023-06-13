from phonemizer import phonemize
import sys

# Access command-line arguments
args = sys.argv
filename = args[1]

backend='espeak'
if "eng" in filename:
    language = "en-us" 
elif "arabic" in filename:
    language = "ar"

# Declare word list and lemma list
words = []
lemmas = []

with open(filename, "r") as file:
# Read file line by line
    lines = file.readlines()

# Parse word and lemma from line; add to word list and lemma list
    for line in lines[1:]:
        tokens = line.split("\t")
        if language == "en-us":
            words.append(tokens[0])
            lemmas.append(tokens[1])
        elif language == "ar":
            words.append(tokens[1])
            lemmas.append(tokens[3])

# Create transcriptions for word list and lemma list 
words_trans = phonemize(words, language, backend)
lemmas_trans = phonemize(lemmas, language, backend)

print(words_trans)
print(lemmas_trans)