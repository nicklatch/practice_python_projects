# List Overlap
import random


def lst_overlap(l1, l2):
    ol_lst = []
    comb_list = l1 + l2
    for i in comb_list:
        if comb_list.count(i) != 1:
            ol_lst.append(i)
    return list(set(ol_lst))


# test
lst_one = random.sample(range(1, 6), random.randint(1, 5))
lst_two = random.sample(range(1, 6), random.randint(1, 5))

print(lst_one, lst_two, lst_overlap(lst_one, lst_two))
