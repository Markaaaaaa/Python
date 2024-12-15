def second_largest(numbers):
    largest = second = float('-inf') 
    for num in numbers:
        if num > largest:  
            second = largest
            largest = num
        elif num > second and num != largest:  
            second = num
    return second

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"The second largest number is: {second_largest(numbers)}")
