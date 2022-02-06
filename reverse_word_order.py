# Reverse Word Order


def rev_ord(s):
    ss = s.split(" ")
    return " ".join(ss[::-1])


print(rev_ord("My name is Nick"))
