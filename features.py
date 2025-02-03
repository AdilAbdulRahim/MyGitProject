def play_again():
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice in ["yes", "no"]:
            return choice == "yes"
        else:
            print("Please enter 'yes' or 'no'.")

def update_score():
  if high_score is None or attempts < high_score:
            high_score = attempts
            print("New high score!")

        print(f"Currently, high score is {high_score} attempts.")

        if not play_again():
            print("Thanks for playing! Goodbye!")
            break
