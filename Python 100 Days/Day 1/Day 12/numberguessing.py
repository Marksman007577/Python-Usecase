# Python 3!
# Author: Mark O. C
# Project: Number guessing game

from art import logo
import random

easy_mode = 10
medium_mode = 7
hard_mode = 5


def set_mode():
    mode_select = input("Select your difficulty level 'Easy', 'Medium', or 'Hard':\t").lower()
    if mode_select == "easy":
        return easy_mode
    elif mode_select == "medium":
        return medium_mode
    else:
        return hard_mode


def compare_answer(my_number, computer_number, trial):
    if my_number > computer_number:
        print("The number is too high")
        return trial - 1

    elif my_number < computer_number:
        print("The number is too low")
        return trial - 1

    elif my_number == computer_number:
        print(f"You are correct!!. The number is {computer_number}")


def num_guess():
    print(logo)
    print("Number guessing game")
    print(" ")
    print("I am thinking of a number between 1 and 100!.")

    computer_number = random.randint(1, 101)

    trial = set_mode()

    my_number = 0

    while my_number != computer_number:
        print(f"You have {trial} attempts to make the correct guess")
        my_number = int(input("Make a guess: \t"))

        trial = compare_answer(my_number, computer_number, trial)

        if trial == 0:
            print("You have no more guesses. You loose")

        elif my_number != computer_number:
            print("Make another guess")


num_guess()
