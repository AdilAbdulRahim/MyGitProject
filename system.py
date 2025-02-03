#validation sys function 
highScore = None
def validateInput(userInput):
    try:
        guess = int(userInput)
        if 1 <= guess <= 100:
            return guess
        else:
            print("Please enter a number between 1 and 100.")
            return None
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

#scoring system function
def updateScoringSystem(attempts):
    global highScore
    if highScore is None or attempts < highScore:
        highScore = attempts
        print(f"New high score! You set the record with {highScore} attempts.")
    else:
        print(f"Current high score is {highScore} attempts.")
