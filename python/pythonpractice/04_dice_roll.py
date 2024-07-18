import random
import time


class Dicegame:
    def __init__(self, rounds=10):
        self.rounds = rounds
        self.player1_sum = 0
        self.player2_sum = 0
        self.player1_win = 0
        self.player2_win = 0

    def play_round(self):
        player1 = random.randint(1, 6)
        player2 = random.randint(1, 6)
        return player1, player2

    def play_game(self):

        print(
            "Player1 and Player2 are playing 10 rounds of Dice game and below are the results:\n"
        )

        for round_num in range(1, self.rounds + 1):
            player1, player2 = self.play_round()
            self.player1_sum += player1
            self.player2_sum += player2

            input(f"Press Enter to play round {round_num}")
            print("Dice Rolling...\n")
            time.sleep(1)
            print(f"Player1- {player1}  Player2- {player2}", end="  ")

            if player1 == player2:
                print(f"{round_num}th Round: DRAW")
            elif player1 > player2:
                print(f"{round_num}th Round: Player1 Wins\n")
                self.player1_win += 1
            else:
                print(f"{round_num}th Round: Player2 Wins\n")
                self.player2_win += 1

    def display_result(self):
        if self.player1_win == self.player2_win:
            print("\nAverage Result: DRAW\n")
        elif self.player1_win > self.player2_win:
            print(
                f"\nPlayer1 WINS\nWinning Counts are:\nPlayer1 won {self.player1_win} times.\nPlayer2 won {self.player2_win} times."
            )
        else:
            print(
                f"\nPlayer2 WINS\nWinning Counts are:\nPlayer2 won {self.player2_win} times.\nPlayer1 won {self.player1_win} times."
            )

        print(f"Player1 Average Points = {self.player1_sum}")
        print(f"Player2 Average Points = {self.player2_sum}")


# Directly calling the main logic to run the game
game = Dicegame()
while True:
    game.play_game()

    ch = input("\nWant to play Again? (Y/N) ").strip()
    if ch not in "Yy":
        break
