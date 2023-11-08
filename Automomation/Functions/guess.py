import random

print("This is a number guessing game\n")
computer_guess = random.randint(1, 20)
print("I am thinking of a number between 1 and 20")

for guess in range(1, 7):
    user_guess = int(input("Take a guess:"))

    if user_guess < computer_guess:
        print("Your guess is too low.\n")

    elif user_guess > computer_guess:
        print("Your guess is too high.\n")

    else:
        print(f"Correct! {user_guess} was my guess\n")
        break

if user_guess == computer_guess:
    print(f"Good job!. You guessed my number in {guess} guesses!")

else:
    print(f"Nope. The number I was thinking of was {computer_guess}")
