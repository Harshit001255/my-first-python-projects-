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
choice = True
while choice == True:
    print("1. C to F\n2. C to K\n3. F to C\n4. K to C\n5. F to K\n6. Exit")

    try:
        option = int(input("Enter your conversion option: "))
    except ValueError as v:
        print("Invalid choice! Please enter a number between 1 and 6.")
        continue

    match option:
        case 1:
            print("Celsius to Fahrenheit:")
            try:
                c = float(input("Enter the value in Celsius: "))
            except ValueError as v:
                print("Error: Please enter a valid numerical temperature value")
                continue
            f = (c*(9/5)) + 32
            print(f"The value in Fahrenheit = {f:.2f}")
            print(".....")
        case 2:
            print("Celsius to Kelvin:")
            try:
                c = float(input("Enter the value in Celsius: "))
            except ValueError as v:
                print("Error: Please enter a valid numerical temperature value")
                continue
            k = c + 273.15
            print(f"The value in Kelvin = {k:.2f}")
            print(".....")
        case 3:
            print("Fahrenheit to Celsius:")
            try:
                f = float(input("Enter the value in Fahrenheit: "))
            except ValueError as v:
                print("Error: Please enter a valid numerical temperature value")
                continue
            c = (f - 32) * 5/9
            print(f"The value in Celsius = {c:.2f}")
            print(".....")
        case 4:
            print("Kelvin to Celsius:")
            try:
                k = float(input("Enter the value in Kelvin: "))
            except ValueError as v:
                print("Error: Please enter a valid numerical temperature value")
                continue
            c = k - 273.15
            print(f"The value in Celsius = {c:.2f}")
            print(".....")
        case 5:
            print("Fahrenheit to Kelvin:")
            try:
                f = float(input("Enter the value in Fahrenheit: "))
            except ValueError as v:
                print("Error: Please enter a valid numerical temperature value")
                continue
            k = ((f - 32) * 5/9) + 273.15
            print(f"The value in kelvin = {k:.2f}")
            print(".....")
        case 6:
            print("Exiting the loop....")
            choice = False
        case _:
            print("Please select a valid option from 1 to 6.")
