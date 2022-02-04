# Check Primality Functions


def ch_prime(n):
    if n > 1:
        if len(a) == 0:
            return "Prime"
    return "Not Prime"


num = int(input("Pick a number to check is primality: "))
a = [i for i in range(2, num) if num % i == 0]
print(ch_prime(num))
