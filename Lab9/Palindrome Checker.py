def is_palindrome(string):
    clean_string = ''.join(char.lower() for char in string if char.isalnum()) #all lowercase ignore spaces
    return clean_string == clean_string[::-1] #palindrome

# Input and Output
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
