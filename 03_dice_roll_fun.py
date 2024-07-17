import random
import time


def dice_roll():
    ramesh = random.randint(1, 6)
    suresh = random.randint(1, 6)
    return ramesh, suresh


def play_game():
    round = 10
    ramesh_sum = 0
    suresh_sum = 0
    ramesh_win = 0
    suresh_win = 0

    print(
        "Ramesh and Suresh are playing 10 rounds of Dice game and below are the results : \n"
    )
    for round_num in range(1, round + 1):
        ramesh, suresh = dice_roll()
        ramesh_sum = ramesh_sum + ramesh
        suresh_sum = suresh_sum + suresh

        ch = input(f"Press Enter to play round {round_num}")
        print("Dice Rolling...\n")
        time.sleep(1)
        print(f"ramesh- {ramesh_sum}  suresh- {suresh_sum}", end="  ")

        if ramesh == suresh:
            print(f"{round_num}th Round: DRAW")
        elif ramesh > suresh:
            print(f"{round_num}th Round: Ramesh Win\n")
            ramesh_win += 1
        else:
            print(f"{round_num}th Round: Suresh Win\n")
            suresh_win += 1

    if ramesh_win == suresh_win:
        print("\n Average Result : DRAW\n")
    elif ramesh_win > suresh_sum:
        print(
            f"\nRamesh WINS \nWinning Counts are : \nRamesh won, {ramesh_win} times. \nSuresh won, {suresh_win} times."
        )
    else:
        print(
            f"\nSuresh WINS \nWinning Counts are : \nSuresh won, {suresh_win} times. \nRamesh won, {ramesh_win} times."
        )

    print(f"Ramesh Average Points = {ramesh_sum}")
    print(f"Suresh Average Points = {suresh_sum}")


while True:
    play_game()

    ch = input("\nWant to play Again ? (Y/N) ")

    if ch not in "Yy":
        break
