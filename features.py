# features.py
def play_again():
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice in ["y", "n"]:
            return choice == "y"
        else:
            print("Please enter 'y' or 'n'.")
