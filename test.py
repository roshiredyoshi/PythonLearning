def median(lst):
    print(lst)
    lst.sort()
    print(lst)
    if len(lst) == 1:
        return lst[0]
    elif len(lst) %2 == 1:
        return lst[int(len(lst) / 2)]
    else:
        return (lst[int(len(lst) / 2)] + lst[int(len(lst) / 2 - 1)]) / 2


print(median([4, 5, 5, 4]))
