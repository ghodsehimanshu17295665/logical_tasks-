import random


def roll_dice():
    return random.randint(1, 6)


def dice_game():
    player_1 = 0
    player_2 = 0
    rounds = 10

    for rounnd_num in range(1, rounds + 1):
        print(f"\nRound: {rounnd_num}")

        # Player 1 rolls the dice

        player1_score = roll_dice()
        player_1 += player1_score
        print(f"Player 1 rolled a {player1_score}")

        # Player 2 rools the dice:

        player2_score = roll_dice()
        player_2 += player2_score
        print(f"Player 2 rolled a {player2_score}")

        if player_1 > player_2:
            print(f"Player 1 wins & score: {player1_score}")
        elif player_1 < player_2:
            print(f"Player 2 wins & score: {player2_score}")
        else:
            print("It's Tie..")

    # Determine the winner
    print("\nFinal Scores:")
    print(f"Player 1: {player_1 }")
    print(f"Player 2: {player_2}")

    if player_1 > player_2:
        print(f"Player 1 wins & score: {player_1}")
    elif player_1 < player_2:
        print(f"Player 2 wins & score: {player_2}")
    else:
        print("It's Tie..")


dice_game()
