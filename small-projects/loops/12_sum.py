# Project 12: Sum of Numbers

# What it does: Adds all numbers from 1 to 100
# Logic:

# Create total variable starting at 0
# Loop from 1 to 100
# Each loop: add current number to total
# After loop: print total

# Key Concepts: for loops, accumulation, range()

total = 0
for i in range(1, 101):
    total += i

print("The total value is", total)