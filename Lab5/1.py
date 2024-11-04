def second_largest(arr):
    elements = list(set(arr))
    if len(elements) < 2:
        return "There is no second largest unique element."
    elements.sort(reverse=True)
    return elements[1]
print(second_largest([7, 12, 3, 111, 12, 3]))
