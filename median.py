def median(lst):
    lst = sorted(lst)
    if len(lst) % 2 == 1:
        return lst[int(len(lst)/ 2)]
    elif len(lst) % 2 == 0:
        x1 = lst[int(len(lst) / 2) - 1]
        x2 = lst[int(len(lst) / 2)]
        return ((x1 + x2) / 2)

print(median([4,5,5,4]))
print(median([1,1,2]))