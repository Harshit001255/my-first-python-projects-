# Project 18: Average Calculator Function

# What it does: Takes list of numbers, calculates average
# Logic:

# Create function that takes a list of numbers
# Add all numbers together (use sum())
# Divide by how many numbers (use len())
# Return the average
# Test with example list of scores

# Key Concepts: Functions, lists, sum(), len()

def average():
    for i in range(1, 11):
        a = float(input(f"Enter no.{i}: "))
        list1.append(a)
    z = sum(list1)/len(list1)
    return z
    

list1 = []

b = print(average())
