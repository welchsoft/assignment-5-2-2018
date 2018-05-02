#import out tempconverter functions
import tempconverter
#take user userInput
userInput = input("is your temperature in Celcius(Enter C) or Farenheit(Enter F)?")
temp = float(input("Enter the temperature"))

#our logic to ahndle which conversion, and the conversions themselves
if userInput == "C" or userInput == "c":
    print(tempconverter.CtoF(temp))
elif userInput == "F" or userInput == "f":
    print(tempconverter.FtoC(temp))
else:
    print("Invalid entry try again")
