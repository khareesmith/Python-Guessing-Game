#
from random import *

min = randrange(10)
max = randrange(11,21)

rand_num = randint(min,max)

print("Hello! Welcome to Kharee's Guessing Game \n")
user_name = raw_input("Input your name: ")

number_of_guesses = 0

if (user_name == "Kharee"):
    print("Greetings " + user_name + "! The secret number is " + str(rand_num) + ". ;)\n\nI'm thinking of a number between " + str(min) + " and " + str(max) + ".\n")
else:    
    print("\nGreetings " + user_name + "!\n\nI'm thinking of a number between " + str(min) + " and " + str(max) + ".\n")

while number_of_guesses <= 5:

    if(number_of_guesses == 5):
        print("Sorry, you're out of guesses! The number was: " + str(rand_num))
        break

    print("You have " + str(5 - (number_of_guesses)) + " guesses!")
    user_guess = int(raw_input("Input a number: "))

    
    if (user_guess < rand_num):
        print("You are too low!")
        number_of_guesses+=1
    elif(user_guess > rand_num):
        print("Oops too high!")
        number_of_guesses+=1
    elif(user_guess == rand_num):
        print("You guessed correctly! Only took " + str(number_of_guesses + 1) + " tries!")
        break
    
