# RPS Game
import sys

print("ROCK, PAPER, SCISSORS")
print("To quit, you must both enter QUIT")

# Player 1
p1_wins = 0
p1_losses = 0
p1_ties = 0

# Player 2
p2_wins = 0
p2_losses = 0
p2_ties = 0

while True:  # Main game loop
    print(
        "Player 1 has "
        + str(p1_wins)
        + " Wins, "
        + str(p1_losses)
        + " Losses, and "
        + str(p1_ties)
        + " Ties!"
    )
    print(
        "Player 2 has "
        + str(p2_wins)
        + " Wins, "
        + str(p2_losses)
        + " Losses, and "
        + str(p2_ties)
        + " Ties!"
    )
    print()
    while True:  # Player input loop
        p1 = input(
            "Player 1, chose your move wisely! \
            | ROCK, PAPER, OR SCISORS: "
        ).upper()
        p2 = input(
            "Player 2, chose your move wisely! \
            | ROCK, PAPER, OR SCISORS: "
        ).upper()
        print()
        if p1 == "QUIT" or p2 == "QUIT":
            sys.exit()
            break

        # Scoring
        if p1 == p2:
            print(p1 + " vs " + p2 + "...It's a tie!")
            print()
            p1_ties += 1
            p2_ties += 1
        elif p1 == "ROCK" and p2 == "SCISSORS":
            print(p1 + " vs " + p2 + "...Player 1 Wins!")
            print()
            p1_wins += 1
            p2_losses += 1
        elif p1 == "PAPER" and p2 == "ROCK":
            print(p1 + " vs " + p2 + "...Player 1 Wins!")
            print()
            p1_wins += 1
            p2_losses += 1
        elif p1 == "SCISSORS" and p2 == "PAPER":
            print(p1 + " vs " + p2 + "...Player 1 Wins!")
            print()
            p1_wins += 1
            p2_losses += 1
        elif p2 == "ROCK" and p1 == "SCISSORS":
            print(p1 + " vs " + p2 + "...Player 2 Wins!")
            print()
            p2_wins += 1
            p1_losses += 1
        elif p2 == "PAPER" and p1 == "ROCK":
            print(p1 + " vs " + p2 + "...Player 2 Wins!")
            print()
            p2_wins += 1
            p1_losses += 1
        elif p2 == "SCISSORS" and p1 == "PAPER":
            print(p1 + " vs " + p2 + "...Player 2 Wins!")
            print()
            p2_wins += 1
            p1_losses += 1
