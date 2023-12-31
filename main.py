from phonemizer import phonemize
import sys

# Access command-line arguments
args = sys.argv
filename = args[1]

# Create output file with word transcriptions
newFilename = filename+".out"
newFile = open(newFilename, "w")

# Set variables for phonemize
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

# TODO: Add word transcriptions to input file
    for i in range(len(lines)):
        line = lines[i]
        tokens = line.split("\t")
        newFile.write(tokens[0]+"\t") # write word to new file
        if (i == 0): # Write headers
            newFile.write("transcription\t")
        else:
        # Write word's transcription in second column
            newFile.write(words_trans[i-1]+"\t") 
        # Write rest of columns to file 
        for j in range(1, len(tokens)):
            newFile.write(tokens[j])
            if j != len(tokens)-1:
                newFile.write("\t")