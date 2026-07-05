# Project 4: Simple Unit Converter

# What it does: Converts one unit to another (miles to km, pounds to kg, etc.)
# Logic:

# Ask user for distance in one unit
# Store conversion rate as variable (e.g., 1 mile = 1.60934 km)
# Multiply input by conversion rate
# Print result

# Key Concepts: Variables, multiplication, float handling


k = float(input("Enter distance in kilometers: "))
mile = 1.60934
print(f"{k} kilometers is equal to {k/mile:.2f} miles.")
