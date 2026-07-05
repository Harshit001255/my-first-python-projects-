# Project 3: BMI Calculator

# What it does: Calculates Body Mass Index from weight and height
# Logic:

# Ask user for weight (in kg)
# Ask user for height (in meters)
# Calculate: BMI = weight ÷ (height × height)
# Print result with 2 decimal places


# Key Concepts: Float conversion, math operations, formatting numbers

w = float(input("Enter Weight (kg): "))
h = float(input("Enter height (meters): "))
BMI = w/(h*h)
print(f"the BMI value is {BMI:.2f}")