# Reverse Word Order


def rev_ord(s):
    return " ".join(s.split(" ")[::-1])


print(rev_ord("My name is Nick"))
