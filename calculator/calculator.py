#function to take input from user
def userInput():
    first_number = float(input("Enter the first number: "))
    operand = input("Enter the operand (+,-,*,/): ")
    second_number = float(input("Enter the second number: "))
    return first_number,operand,second_number

#function to display the results
def displayResult(first_number,operand, second_number, result):
    print(f"{first_number} {operand} {second_number} = {result}")

#function for adding
def add(first_number,second_number):
    return first_number + second_number

#function for subtracting
def subtract(first_number,second_number):
    return first_number - second_number

#function for multiplying
def multiply(first_number,second_number):
    return first_number * second_number

#function for dividing
def divide(first_number,second_number):
    return first_number / second_number
