def prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1): #a number has a divisor larger than its square root, the corresponding smaller divisor would have already been found.
        if number % i == 0:
            return False
    return True

# Input and Output
number = int(input("Enter a number: "))
if prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
