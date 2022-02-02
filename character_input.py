# Character Input
def char_in(name, age, year, bday):
    if bday.upper() == 'Y':
        return(name + " you will turn 100 in the year " + str((year - age) + 100))
    else:
        return(name + " you will turn 100 in the year " + str((year - age) + 99))


print(char_in(input("What is your name? "),
      (int(input("How old are you? "))), int(input("What year is it? ")), input("Have you had your birthday yet this year? (Y/N) ")))
