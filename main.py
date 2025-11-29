import random

def intro():
    print("Welcome to the Reverse Guessing Game")
    print("""
How to play:
- Pick a secret number between 1 and 100
- The computer will try to guess it
""")

def get_valid_number():
    while True:
        try:
            number = int(input('Choose your number (1-100): '))
            if 0 < number <= 100:
                return number
            else:
                print("Number must be between 1 and 100.")
        except ValueError:
            print("Only numbers are allowed")


def guessing_game(number):

    left = 1
    right = 100
    attempts = 0

    while left <= right:
        computer_picked = random.randint(left,right)
        attempts += 1
        if computer_picked == number:
            return (computer_picked,attempts)
        if computer_picked > number:
            right = computer_picked - 1
        else:
            left = computer_picked + 1

def main():
    intro()
    while True:
        number = get_valid_number()
        guessed,tries = guessing_game(number)

        print(f"\nComputer guessed correctly in {tries} turns!")
        print(f"Your number was: {guessed}")

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing this game!")
            break

if __name__ == "__main__":
    main()
    
