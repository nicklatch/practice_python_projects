# List Less Than Ten

def less_than_ten(list, num):
    return [i for i in list if i < num]


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("Pick a number between 1 and 89: "))
print(less_than_ten(a, num))
