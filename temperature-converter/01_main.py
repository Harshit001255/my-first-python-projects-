# Portfolio Project #1: Temperature Converter
# What it does: Menu-driven app that converts between Celsius, Fahrenheit, Kelvin
# How it works:

# Show menu with 5 conversion options
# User picks option (1-5)
# Based on choice:

# Ask for temperature value
# Convert using correct formula
# Print result with 2 decimal places

# After conversion, show menu again
# Loop until user exits

# Formulas needed:

# C to F: (C × 9/5) + 32
# C to K: C + 273.15
# F to C: (F - 32) × 5/9
# K to C: K - 273.15
# F to K: (F - 32) x 5/9 + 273.15

# Key Concepts:

# Menu-driven loops
# Multiple conversion functions
# Error handling (try/except for invalid input)
# String formatting with decimals
# f-strings

print("1. C to F\n2. C to K\n3. F to C\n4. K to C\n5. F to K")

option = int(input("Enter your conversion option: "))

match option:
    case 1:
        print("Celsius to Fahrenheit:")
        c = float(input("Enter the value in Celsius: "))
        f = (c*(9/5)) + 32
        print(f"The value in Fahrenheit = {f}")
    case 2:
        print("Celsius to Kelvin:")
        c = float(input("Enter the value in Celsius: "))
        k = c + 273.15
        print(f"The value in Kelvin = {k}")
    case 3:
        print("Fahrenheit to Celsius:")
        f = float(input("Enter the value in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"The value in Celsius = {c}")
    case 4:
        print("Kelvin to Celsius:")
        k = float(input("Enter the value in Kelvin: "))
        c = k - 273.15
        print(f"The value in Celsius = {c}")
    case 5:
        print("Fahrenheit to Kelvin:")
        f = float(input("Enter the value in Fahrenheit: "))
        k = ((f - 32) * 5/9) + 273.15
        print(f"The value in Celsius = {k}")
    