# Fibonacci


def fib_func():
    ui = int(input("How long of a Fibonacci sequence would you like? "))
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


# ui = int(input("How long of a Fibonacci sequence would you like? "))
print(fib_func())
