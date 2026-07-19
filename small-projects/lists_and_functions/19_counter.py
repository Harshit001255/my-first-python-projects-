# Project 19: Word Counter

# What it does: Counts how many times each word appears in a sentence
# Logic:

# Ask user for a sentence
# Split sentence into words (split by spaces)
# Loop through each word:

# If word already in dictionary: add 1 to count
# If word new: add to dictionary with count = 1

# Print each word with its count

# Key Concepts: Dictionaries, loops, string split(), if conditions

text = input("Enter a sentence: ")
word = text.split(" ")
dict = {}
for word in word:
    if(word in dict):
        dict[word] = dict[word] + 1
    else:
        dict[word] = 1

print(dict)

                    

