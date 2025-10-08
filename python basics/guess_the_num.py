import random
guessedNum = input("guess the number (1 to 10): ")
number = random(10)
if number == guessedNum:
    print(f"You guessed right the num is {number}")
else:
    print("You guessed wrong")

