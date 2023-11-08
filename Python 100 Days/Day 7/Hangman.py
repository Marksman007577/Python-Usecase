from Hangman_word import word_list
from Hangman_art import logo
from Hangman_art import stages
import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
end_of_game = False

display = []
for _ in range(word_length):
    display += "-"

print(logo)
# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    # requesting the user input
    guess = input("Guess a letter: ").lower()
    # check if letter has been guessed before
    if guess in display:
        print(f"You've already guessed {guess}")
    # checking if the letter guessed is in the computer choice
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # checking if guess not in display
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    # checking if there are still more blank spaces
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])