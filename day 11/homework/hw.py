#დავალება 1


import random

def number_guess_game_if_else():
    number_to_guess = random.randint(1, 100)
    print("Welcome to the Number Guess Game! Guess the number between 1 and 100.")
    
    while True:
        guess = int(input("Enter your guess: "))
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the right number!")
            break

number_guess_game_if_else()

#დავალება 2


