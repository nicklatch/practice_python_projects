# RPS Game

print("ROCK, PAPER, SCISSORS")

while True:
    # Player 1
    p1_wins = 0
    p1_losses = 0
    p1_ties = 0

    # Player 2
    p2_wins = 0
    p2_losses = 0
    p2_ties = 0

    # Stats Print
    print("Player 1 has " + str(p1_wins) + " Wins, " +
          str(p1_losses) + " Losses, and " + str(p1_ties) + " Ties!")
    print()
    print("Player 1 has " + str(p2_wins) + " Wins, " +
          str(p2_losses) + " Losses, and " + str(p2_ties) + " Ties!")
    print()

    # Player Input
    p1 = input("Player 1, chose your move wisely! | ROCK, PAPER, OR SCISORS: ")
    p2 = input("Player 2, chose your move wisely! | ROCK, PAPER, OR SCISORS: ")

    if p1 == p2:
        p1_ties += 1
        p2_ties += 1
        print(p1 + " vs " + p2 + "...It's a ties!")
        print()

    elif p1 == "r" and p2 == "s":
        p1_wins += 1
