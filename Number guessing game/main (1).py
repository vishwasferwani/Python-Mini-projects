
from art import logo
import random

hard_lives= 5
easy_lives = 10

def difficulty():
    """check difficulty"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'").lower()
    if difficulty == "easy":
        return easy_lives
    else:
        return hard_lives


def compare(guess,random_num,lives):
    """compare user guess and selected no."""
    if guess > random_num:
        print("Too high")
        return lives - 1

    elif guess < random_num:
        print("Too Low")
        return lives -1

    else :
        print("You got it 🎉")

def game():
    print(logo)
    print("Welcome to Number Guessing Game!")
    print("i'm thinking of a number between 1 to 100.")

    random_num = random.randint(0,100)
    print(random_num)
    lives = difficulty()
    guess = 0
    while guess != random_num:
        print(f"you have {lives} attempts left")
        guess = int(input("Make a guess"))
        lives = compare(guess,random_num,lives)

        if lives == 0:
            print("You've run out of guesses, you lose.")
            return

        elif guess !=random_num:
            print("Guess again.")

game()

    
    

    
    