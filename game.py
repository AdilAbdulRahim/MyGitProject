import random
from system import validate_input, update_scoring_system
from features import play_again

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    while True:
        user_input = input("Enter your guess: ")
        guess = validate_input(user_input)

        if guess is None:
            continue  # Skip invalid input

        attempts += 1

        if guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            update_scoring_system(attempts)
            if not play_again():
                print("Thanks for playing! Goodbye!")
                break
            else:
                # Reset the game for a new round
                number = random.randint(1, 100)
                attempts = 0
                print("\nNew round! I am thinking of a number between 1 and 100.")


number_guessing_game()
