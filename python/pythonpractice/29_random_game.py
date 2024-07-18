import random

print(
    """
A Number is stored in range 1-200,
You have to guess the Number in minimum chances
All the Best!
"""
)


def guess_number_game():
    # The number to be guessed, randomly chosen
    guess_number = random.randint(1, 200)
    chance = 0

    while True:
        user_guess = int(input("Enter Your choice Number : "))
        chance = chance + 1

        if user_guess < 1 or user_guess > 200:
            print("Please enter a number within the range 1-200.")
            continue

        if user_guess < guess_number:
            print("Too Small")
        elif user_guess > guess_number:
            print("Too Large")
        else:
            print(f"Congratulations you got the number in {chance} chances")
            break


while True:
    guess_number_game()
    choice = input("Play Again (y/n)? : ")
    if choice not in 'yY':
        break
