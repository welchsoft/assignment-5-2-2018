#function to take user user input
def userInput():
    user_input = input("is your temperature in Celcius(Enter C) or Farenheit(Enter F)? ")
    temperature = float(input("Enter the temperature: "))
    return user_input, temperature

#function for Farenheit to Celcius
def CtoF(temperature):
    return (temperature * 1.8 + 32)
#function for Celcius to Farenheit
def FtoC(temperature):
    return ((temperature - 32)/1.8)
