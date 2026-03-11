# Number Guessing Game
# Computer selects a random number, user has to guess it

import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    print("\nWelcome to Number Guessing Game!")
    print("Guess the number between 1 and 100.")

    while True:
        guess_input = input("Enter your guess: ").strip()
        if not guess_input.isdigit():
            print("Please enter a valid number!")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break

while True:
    play_game()
    again = input("\nDo you want to play again? (y/n): ").strip().lower()
    if again != 'y':
        print("Thanks for playing! Bye!")
        break