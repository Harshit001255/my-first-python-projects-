# Project 6: Even or Odd Checker

# What it does: Takes a number, tells if it's even or odd
# Logic:

# Get number from user
# Check: if number divided by 2 has remainder 0 → even
# Otherwise → odd
# Print result

# Key Concepts: if/else, modulo operator (%)

n = int(input("Enter a number: "))
if(n%2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")