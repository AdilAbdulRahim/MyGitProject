high_score = None
#validate
def validate_input(user_input):
    try:
        guess = int(user_input)
        if 1 <= guess <= 100:
            return guess
        else:
            print("Please enter a number between 1 and 100.")
            return None
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None
#update score
def update_scoring_system(attempts):
    global high_score
    if high_score is None or attempts < high_score:
        high_score = attempts
        print(f"New high score! You set the record with {high_score} attempts.")
    else:
        print(f"Current high score is {high_score} attempts.")
