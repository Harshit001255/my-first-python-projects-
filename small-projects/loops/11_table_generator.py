# Project 11: Multiplication Table Generator

# What it does: Shows multiplication table for a number
# Logic:

# Get a number from user
# Loop from 1 to 10
# For each number: multiply by user's number, print result
# Example: 5×1=5, 5×2=10, 5×3=15... etc


# Key Concepts: for loops, range(), multiplication

n = int(input("Enter a Number: "))
print(f"The table for number {n} is...")
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

