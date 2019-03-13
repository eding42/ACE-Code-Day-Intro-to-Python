# Import the python builtin math library
import math

# Get inputs (first number, second number, operation)
num1 = input("Input a number:")
num2 = input("Input another number:")
op = input("Input an operation:")

# Convert num1 and num2 to integers (whole numbers)
num1 = int(num1)
num2 = int(num2)

if op == "+":
    # If the user inputted + (add), add the numbers
    print(num1 + num2)
elif op == "-":
    # If the user inputted - (subtract), subtract
    # num2 from num1

    # NOTE: We use ELIF here to make it clear that op
    # can only be one sign, not multiple
    # While IF would still work in this case, ELIF
    # makes it more clear to other people reading your code 
    print(num1 - num2)
elif op == "*":
    # If the user inputted * (multiply), multiply the numbers
    print(num1 * num2)
elif op == "/":
    # If the user inputted / (divide), divide num1 by num2
    print(num1 / num2)
else:
    # If the user didn't input a recognized operation, quit
    print("Operation not recognized! I'm going to kill myself now.")
