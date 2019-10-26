# Program for simple calculator

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def diff(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

print("Please select operation:", "1) Add", "2) Subtract","3) Multiply","4) Divide")
operation = input("Select operations form 1, 2, 3, 4 :")
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if operation == '1':
    print(number1, "+", number2, "=", add(number1, number2))

elif operation == '2':
    print(number1, "-", number2, "=", diff(number1, number2))

elif operation == '3':
    print(number1, "*", number2, "=", multiply(number1, number2))

elif operation == '4':
    print(number1, "/", number2, "=", divide(number1, number2))
else:
    print("Invalid")
