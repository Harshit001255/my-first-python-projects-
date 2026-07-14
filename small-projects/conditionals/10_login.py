# Project 10: Simple Login

# What it does: Asks for password, checks if correct
# Logic:

# Store correct password in variable
# Ask user for password
# If user password equals stored password → "Access granted"
# Else → "Access denied"


# Key Concepts: String comparison, if/else

correct_password = "sharma.harshit@20053009"

password = input("Enter Password: ")
if password == correct_password:
    print("Access Granted...")
else:
    print("Access Denied...")