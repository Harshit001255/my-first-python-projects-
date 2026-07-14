# Project 9: Temperature Alert

# What it does: Takes temperature, shows appropriate alert
# Logic:

# Get temperature in Celsius
# Check conditions:

# if > 40 → extreme heat warning
# if > 30 → hot warning
# if < 0 → freezing warning
# else → comfortable

# Print appropriate message

# Key Concepts: Multiple if/elif conditions, practical application

temp = float(input("Enter the Temperature: "))
if temp > 40:
    print("Extreme Heat!!")
elif temp < 40 and temp > 30:
    print("Hot!!")
elif temp < 0:
    print("Freezing!!")
else:
    print("Comfortable!!")
    