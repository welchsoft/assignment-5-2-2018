#take input from user
userInput = int(input("please input a number "))
# if its divisible by 15 fizzbuzz, by 3 fizz, by 5 buzz, else just be rude
if userInput % 15 == 0:
    print("Fizz Buzz ")
elif userInput % 3 == 0:
    print("Fizz ")
elif userInput % 5 == 0:
    print("Buzz ")
else:
    print("you entered " + str(userInput) + " and thats just no good")
