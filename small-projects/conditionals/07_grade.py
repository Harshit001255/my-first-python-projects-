# Project 7: Grade Calculator

# What it does: Takes a score (0-100), assigns letter grade
# Logic:

# Get score from user
# Check multiple conditions:

# Score ≥ 90 → A
# Score ≥ 80 → B
# Score ≥ 70 → C
# Score < 70 → F

# Print letter grade

# Key Concepts: if/elif/else chains, comparison operators
# small-projects\conditionals\06_even_odd.py

score = int(input("Enter your score (0-100): "))
if score >= 90:
    print("Your grade is A.")
elif score >= 80:
    print("Your grade is B.")
elif score >= 70:
    print("Your grade is C.")
else:
    print("Your grade is F.")