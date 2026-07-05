# Project 5: Age in Different Units

# What it does: Takes age in years, converts to days, hours, minutes
# Logic:

# Ask user for age in years
# Calculate: days = years × 365
# Calculate: hours = days × 24
# Calculate: minutes = hours × 60
# Print all values

# Key Concepts: Sequential calculations, variables, multiplication

y = int(input("Enter your age in years: "))
days = y * 365
hours = days * 24
min = hours * 60 
print(f"your age of {y} years is equivalent to {days} days, {hours} hours, and {min} minutes.")