def has_duplicates(ary):
    return len(ary) != len(set(ary))
print(has_duplicates([1, 6, 3, 7, 5]))
print(has_duplicates([1, 6, 3, 7, 1]))
