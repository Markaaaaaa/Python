def intersection(arr1, arr2):
    set1= set(arr1)
    set2= set(arr2)
    return list(set1 & set2)
print(intersection([3, 2, 1, 3,4], [6, 2, 3, 4, 1]))
