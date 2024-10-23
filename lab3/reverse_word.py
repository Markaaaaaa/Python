def reverse_string(s):
    return s[::-1]


from reverse_string import reverse_string
user_input = input("Enter a string to reverse: ")
reversed_string = reverse_string(user_input)
print(f"Reversed string: {reversed_string}")
