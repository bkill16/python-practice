import random

random_number = random.randint(1, 100)
user_guess = 0

while user_guess != random_number:
    user_guess = int(input("Guess a number between 1 and 100: "))

    if (user_guess > random_number):
        print("Lower")
    if (user_guess < random_number):
        print("Higher")
    if (user_guess == random_number):
        print("Good job! You guessed it!")
        break