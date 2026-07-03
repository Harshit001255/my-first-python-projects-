# Project 1: Personal Greeter

# What it does: Takes your name and age as input, calculates birth year, prints personalized message
# Logic:

# Ask user for name (store in variable)
# Ask user for age (store in variable)
# Calculate birth year (current year - age)
# Print: "Hello [name]! You were born in [birth year]"


# Key Concepts: Variables, input(), arithmetic, string formatting

n = input("What is your name? ")
a = int(input("What is your age? "))
current_year = 2026
birth_year = current_year - a
print(f"Hello {n}! you were born in {birth_year}.")