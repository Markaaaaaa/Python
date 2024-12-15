def second_largest(numbers):
    largest = second = float('-inf') # Initialize to negative infinity
    for num in numbers:
        if num > largest: # Found a new largest number 
            second = largest
            largest = num
        elif num > second and num != largest:  # Found a new second largest
            second = num
    return second

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"The second largest number is: {second_largest(numbers)}")
