from random import *

min = randint(0,10)
max = randint(11,20)

rand_num = randint(min,max)

print("Hello! Welcome to Kharee's Guessing Game \n")
user_name = raw_input("Input your name: ")

number_of_guesses = 0

print("\nGreetings " + user_name + "!\n\nI'm thinking of a number between " + str(min) + " and " + str(max) + ".\n")

while number_of_guesses < 5:
    print("You have " + str((5 - number_of_guesses)) + " guesses!")
    user_guess = int(raw_input("Input a number: "))

    if(number_of_guesses == 5):
        print("Sorry, you're out of guesses! The number was: " + rand_num)
    elif (user_guess < rand_num):
        print("Too low, try again!")
        number_of_guesses+=1
    elif(user_guess > rand_num):
        print("Too high, try again!")
        number_of_guesses+=1
    else:
        print("You guessed correctly! Only took " + str(number_of_guesses) + " tries!")
        break
