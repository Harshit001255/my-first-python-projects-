# Project 17: List of Favorites

# What it does: Asks user for favorite things, stores in list, prints them back
# Logic:

# Create empty list
# Loop 3 times:

# Ask user for one favorite thing
# Add to list (append)

# Loop through list:

# Print each item with "-" prefix

# Key Concepts: Lists, append(), loops, list iteration

list1 = []

for i in range(1, 4):
    s = input(f"Enter your no. {i} favourite Sport: ")
    list1.append(s)

for j in list1:
    print("-", j)