# Project 2: Mad Libs Game

# What it does: Asks user for random words (noun, verb, adjective), fills them into a story
# Logic:

# Ask for 3-4 different types of words
# Store each in separate variable
# Print a pre-written sentence/story using those variables
# Example: "The [adjective] [noun] started to [verb]!"


# Key Concepts: String interpolation, input(), variables

ad = input("Enter an adjective: ")
n = input("Enter a noun: ")
v = input("Enter a verb: ")
print(f"The {ad} {n} started to {v}!")