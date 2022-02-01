# Guess the Number Game

import random

# Welcoming the users
print("Welcome to our Guessing Game! Let's play!")
print("------------------------------------------")

difficulty = input("Please choose a difficulty level (easy, normal, hard): ")

if difficulty == 'easy':
    guesses = 10
elif difficulty == 'normal':
    guesses = 5
elif difficulty == 'hard':
    guesses = 3
else:
    print("Invalid input")

print("You have " + str(guesses) + " tries to guess the correct answer.")

random_number = random.randint(1,100)
user_guess = 0

while user_guess != random_number and guesses != 0:
    user_guess = int(input("Guess a number between 0 and 100: "))
    if user_guess < random_number:
        print("Sorry, guess again. Too low.")
        guesses = guesses - 1
        print("You have " +  str(guesses) + " guesses left!")
        print("++++++++++++++++++++++++++++++++++++++++++")
    elif user_guess > random_number:
        print("Sorry, guess again. Too high.")
        guesses = guesses - 1
        print("You have " + str(guesses) + " guesses left!")
        print("++++++++++++++++++++++++++++++++++++++++++")
    else:
        print("Great work detective! You guessed the number " + str(random_number) + " correctly!")
