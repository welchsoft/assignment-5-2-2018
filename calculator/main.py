import calculator

#take user input
firstNumber = float(input("Enter the first number"))
operand = str(input("Enter the operand"))
secondNumber = float(input("Enter the second number"))

#check the operand against available functions and run it if possible
if operand == "+":
    print(calculator.add(firstNumber, secondNumber))
elif operand == "-":
    print(calculator.subtract(firstNumber, secondNumber))
elif operand == "*":
    print(calculator.multiply(firstNumber, secondNumber))
elif operand == "/":
    print(calculator.divide(firstNumber, secondNumber))
else:
    print("invalid operand")
