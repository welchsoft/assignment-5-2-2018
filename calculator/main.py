import calculator

#take user input
(first_number,operand,second_number) = calculator.userInput()

#result variable
result = 0.0

#check the operand against available functions and run it if possible
if operand == "+":
    result = calculator.add(first_number, second_number)
elif operand == "-":
    result = calculator.subtract(first_number, second_number)
elif operand == "*":
    result = calculator.multiply(first_number, second_number)
elif operand == "/":
    result = calculator.divide(first_number, second_number)
else:
    print("Error: invalid operand ")

#display the result
calculator.displayResult(first_number,operand,second_number, result)
