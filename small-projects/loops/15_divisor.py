# Project 15: Find Divisors

# What it does: Finds all numbers that divide evenly into a number
# Logic:

# Get a number from user
# Loop from 1 to that number
# For each loop number: check if it divides evenly (no remainder)
# If yes: print it
# Result: all divisors printed

# Key Concepts: for loops, modulo operator, if conditions

n = int(input("Enter a number: "))
for i in range(1, n+1):
    if(n%i == 0):
        print(i)
    else:
        continue

