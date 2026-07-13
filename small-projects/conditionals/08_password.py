# Project 8: Password Validator

# What it does: Checks if password is strong (8+ chars, has numbers)
# Logic:

# Get password from user
# Check length: if less than 8 → print "too short"
# Check if contains digits: if no → print "add numbers"
# If both pass → print "strong password"

# Key Concepts: Logical operators (and/or), string methods
# small-projects\conditionals\06_even_odd.py

password = input("Enter a password: ")
if(len(password) < 8):
    print("Password is too short.")
elif not any(char.isdigit() for char in password):
    print("Add numbers.")
else:
    print("Strong password.")