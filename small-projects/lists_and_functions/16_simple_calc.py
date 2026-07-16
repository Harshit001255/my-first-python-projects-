# Project 16: Simple Calculator Function

# What it does: Creates functions for add/subtract/multiply/divide
# Logic:

# Create function called "add" that takes 2 numbers, returns sum
# Create function called "subtract" that takes 2 numbers, returns difference
# Create function called "multiply" that takes 2 numbers, returns product
# Create function called "divide" that takes 2 numbers, returns quotient
# Test: call each function with example numbers, print results

# Key Concepts: Functions, parameters, return values

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if(y == 0):
        return "Error!!"
    return x/y

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(add(a, b))
print(sub(a, b))
print(mul(a, b))
print(div(a, b))