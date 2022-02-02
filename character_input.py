# Character Input
def char_in():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    year = int(input ("What year is it? "))
    bday = input("Have you had your birthday yet this year? (Y/N) ")
    if bday.upper() == 'Y':
        return(name + " you will turn 100 in the year " + str((year - age) + 100))
    else:
        return(name + " you will turn 100 in the year " + str((year - age) + 99))

print(char_in())