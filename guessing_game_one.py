# Guessing Game One (as a funciton)
import random
import sys


def guess_num(cn):
    guess = 0
    tries = 0
    while guess != cn or "exit":
        # player input
        guess = int(input("What number am I thinking of? Take a guess(1-9)! "))
        if guess == "exit":
            sys.exit()
        elif guess < cn:
            tries += 1
            print("Too Low! Guess again!")
            continue
        elif guess > cn:
            tries += 1
            print("Too High! Guess again!")
            continue
        else:
            if tries == 1:
                return "You guessed my number," + str(cn) + " in " + str(tries) + " try!"
            else:
                return "You guessed my number," + str(cn) + " in " + str(tries) + " tries!"


comp_num = random.randint(1, 9)  # number to guess
print(guess_num(comp_num))
