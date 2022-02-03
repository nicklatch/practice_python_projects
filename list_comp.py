# List Comprehension

def list_comp(l):
    return [i for i in l if i % 2 == 0]


ls = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(list_comp(ls))
