# Character Input

from traceback import print_tb


def char_in(name, age, year):
    return(name + "you will turn 100 in the year " + str((year - age) + 100))


print(char_in(input("What is your name? "),
      (int(input("How old are you? "))), 2022))
