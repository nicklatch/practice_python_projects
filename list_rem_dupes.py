# List Remove Duplicates Solutions


def list_rem_dupes(ls):
    return list(set(ls))


lst = [
    1,
    1,
    2,
    2,
    3,
    3,
    4,
    4,
    5,
    5,
    6,
    6,
    6,
    7,
    7,
    7,
    8,
    9,
    9,
    9,
    10,
    10,
    100,
    101,
    101,
    1,
    2,
    4,
]
print(lst)
print(list_rem_dupes(lst))
