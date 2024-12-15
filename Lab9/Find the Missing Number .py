def missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2 #find the sum from 1 to the length of the string
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

# Input and Output
numbers = list(map(int, input("Enter numbers separated by spaces: ").split())) #make it a list
n = len(numbers) + 1 #there is a missing number 
print(len(numbers))
number = missing_number(numbers, n)
print(f"The missing number is: {number}")
