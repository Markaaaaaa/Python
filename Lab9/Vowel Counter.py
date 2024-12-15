def count_vowels(string):
    vowels = "aeiouAEIOU" #define vowels
    count = 0
    for char in string: #loop
        if char in vowels: #check vowels
            count += 1
    return count

# Input and Output
strings = input("Enter a string: ")
print(f"Number of vowels: {count_vowels(strings)}")
