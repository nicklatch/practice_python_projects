# Odd Or Even
def even_or_odd(n):
    if n % 4 == 0:
        return("Your number is even and divides evenly in to 4!")
    elif n % 2 == 0:
        return("Your number is even!")
    else:
        return("Your number is odd!")


numb = int(input("What is your favorite number? "))
print(even_or_odd(numb))
