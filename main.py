import random

def roll_dice():
    return random.randint(1, 6)

def dice_simulator():
    print("🎲 Welcome to the Dice Rolling Simulator!")

    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled a {result} 🎲")

        choice = input("Roll again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            break


dice_simulator()
