from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")

level = input("Choose a difficulty level. Type 'Easy' or 'Hard'\n")

lives = 10


def live_checker():
    global lives
    if level == "Easy":
        lives = 10
    if level == "Hard":
        lives += -5


live_checker()

import random as rd

computer_num = rd.choice(range(1, 100))

x = True
while x == True:
    if lives == 1:
        x = False

    guess = int(input("Choose a Number:"))
    lives += -1

    if guess == computer_num:
        print("You win")
        x = False
    if guess > computer_num:
        print(f"Too high.\nGuess again\nYou have {lives} attempts remaining to guess the number")

    if guess < computer_num and lives != 0:
        print(f"Too low.\nGuess again\nYou have {lives} attempts remaining to guess the number")

if lives == 0:
    print("oops, you are out of lives\n     GAME OVER")
    

print("Computer guess was", computer_num)

