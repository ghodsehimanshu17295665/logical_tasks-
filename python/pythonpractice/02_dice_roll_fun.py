import random

while True:
    rsum = 0
    ssum = 0
    rwin = 0
    swin = 0
    print(
        "Ramesh and Suresh are playing 10 rounds of Dice game and below are the results : \n"
    )
    for i in range(1, 11):

        ramesh = random.randint(1, 6)
        rsum += ramesh
        suresh = random.randint(1, 6)
        ssum += suresh
        print("ramesh-", ramesh, "  ", "suresh-", suresh, end="  ")

        if ramesh == suresh:
            print("%dth round : DRAW" % i)
        elif ramesh > suresh:
            print("%dth round : Ramesh Wins \n" % i)
            rwin = rwin + 1
        else:
            print("%dth round : Suresh Wins \n" % i)
            swin = swin + 1

    if rwin == swin:
        print("\n Average Result : DRAW\n")
    elif rwin > swin:
        print(
            "\nRamesh WINS \nWinning Counts are : \n Ramesh won ",
            rwin,
            " times. \n Suresh won ",
            swin,
            " times.",
        )
    else:
        print(
            "\nSuresh WINS \nWinning Counts are : \n Ramesh won ",
            rwin,
            " times. \n Suresh won ",
            swin,
            " times.",
        )

    print("Ramesh Average Points = ", rsum)
    print("Suresh Average Points = ", ssum)

    ch = input("\nWant to play Again ? (Y/N)")

    if ch == "y" or ch == "Y":
        pass
    else:
        break
