# Fibonacci


def fib_func(ui):
    fibl = []
    x = 0
    while len(fibl) < ui:
        if x < 2:
            fibl.append(1)
            x += 1
        else:
            fibl.append(fibl[x - 1] + fibl[x - 1])
            x += 1
    return fibl


usn = int(input("How long of a Fibonacci list would you like? "))
print(fib_func(usn))
