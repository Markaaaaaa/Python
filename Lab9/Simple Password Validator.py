def valid_password(password):
    upper = any(char.isupper() for char in password) #check upper
    digit = any(char.isdigit() for char in password) #check digit
    return len(password) >= 8 and upper and digit #all ture

# Input and Output
password = input("Enter a password: ")
if valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
