# String Lists
def palind(string):
    if string.lower() == string[::-1].lower():
        return "Wow, a palindrome!"
    else:
        return "Not a palindrome..."


# test
print(palind(input("Check if your word is a palindrome: ")))
