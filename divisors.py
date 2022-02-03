# Divisors
def div_func(num):
    numl = list(range(1, num + 1))
    divl = []
    for i in numl:
        if num % i == 0:
            divl.append(i)
    return(divl)


# Test
a = int(input("Please Choose a number: "))
print(div_func(a))
