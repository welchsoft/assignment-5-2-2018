#import out tempconverter functions
import tempconverter
#take user userInput
(user_input, temperature) = tempconverter.userInput()

#our logic to handle which conversion, and the conversions themselves
if user_input == "C" or user_input == "c":
    print(tempconverter.CtoF(temperature))
elif user_input == "F" or user_input == "f":
    print(tempconverter.FtoC(temperature))
else:
    print("Invalid entry try again ")
