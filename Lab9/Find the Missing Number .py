def missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

# Input and Output
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
n = len(numbers) + 1
print(len(numbers))
number = missing_number(numbers, n)
print(f"The missing number is: {number}")
