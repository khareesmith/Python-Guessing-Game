#imports everything from the random module. This allows program to select random integers.
from random import *

#Creates min and max variables. Min variable will be between 0 and 10 (not including 10). Max variable will be between 11 and 21 (not including 21).
min = randrange(10)
max = randrange(11,21)

#Creates a random number variable that selects a random integer between the range of the min and max created earlier. The min and max integers are included.
rand_num = randint(min,max)

#Prints welcome message and asks an input for name. Name is saved in variable called user_name.
print("Hello! Welcome to Kharee's Guessing Game \n")
user_name = raw_input("Input your name: ")

#Sets a variable for number of guesses to 0.
number_of_guesses = 0

#Checks if name entered by user is "Kharee". If so, displays message regarding the program having chosen a random number and also what that random number is. If the name is not "Kharee", the program displays the same message about the random number but doesn't display contents.
if (user_name == "Kharee"):
    print("Greetings " + user_name + "! The secret number is " + str(rand_num) + ". ;)\n\nI'm thinking of a number between " + str(min) + " and " + str(max) + ".\n")
else:    
    print("\nGreetings " + user_name + "!\n\nI'm thinking of a number between " + str(min) + " and " + str(max) + ".\n")

#"While" statement that allows code to run while the number of guesses is less than or equal to 5.
while number_of_guesses <= 5:

    #Checks if the number of guesses is equal to 5 and if so, displays a message about what the random number. was.
    if(number_of_guesses == 5):
        print("Sorry, you're out of guesses! The number was: " + str(rand_num))
        break
    
    #Prints message about how many guesses are remaining by subtracting the number of guesses variable from 5.
    print("You have " + str(5 - (number_of_guesses)) + " guesses!")

    #Displays prompt for user's guess of the random number and formats it into an integer.
    user_guess = int(raw_input("Input a number: "))

    #If the user's number is lower than the random number, a message is displayed about it and the number of guesses increases by 1.
    if (user_guess < rand_num):
        print("You are too low!")
        number_of_guesses+=1
    #If the user's number is higher than the random number, a message is displayed about it and the number of guesses increases by 1.
    elif(user_guess > rand_num):
        print("Oops too high!")
        number_of_guesses+=1
    #If the user's number is the same as the random number, a message is displayed that the number was guessed and how many tries it took.
    elif(user_guess == rand_num):
        print("You guessed correctly! Only took " + str(number_of_guesses + 1) + " tries!")
        break
    
