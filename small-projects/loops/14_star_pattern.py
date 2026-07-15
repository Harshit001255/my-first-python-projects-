# Project 14: Star Pattern Generator

# What it does: Prints triangle of stars
# Logic:

# Get number of rows from user
# Loop from 1 to number of rows
# Each loop: print (loop number × star symbol)
# Example: ⭐ then ⭐⭐ then ⭐⭐⭐ (growing triangle)

# Key Concepts: for loops, string multiplication

n = int(input("Enter no. of rows: "))

for i in range(1, n+1):
    print("*"*i)