import random

def number_guessing_game():
  number = random.randit(1,100)
  attemps = 0

  print ("Welcome to the Number Guessing Game!")
  print ("I am thinking of a number between 1 and 100.")

  while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

  if guess < number:
    print("Higher")
  elif guess > number: 
    print ("Lower")
  else: 
    print(f"Congragulation! You guessed the number in {attempts} attempts.")
    break

