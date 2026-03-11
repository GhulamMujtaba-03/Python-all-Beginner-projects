import random

print("Welcome to Dice Rolling Simulator!")

while True:
    roll = input("Press Enter to roll the dice or type 'quit' to exit: ").lower()
    
    if roll == "quit":
        print("Thanks for playing! Goodbye!")
        break

    dice = random.randint(1, 6)
    print(f"You rolled a {dice}!")
    print("-" * 30)