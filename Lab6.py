user_account = {"balance": 1000, "pin": 1234}

def menu():
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")

def check_balance():
    print(f"Your current balance is: ${user_account['balance']}")

def deposit_money():
    try:
        amount = float(input("Enter the amount to deposit: $"))
        user_account["balance"] += amount
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def withdraw_money():
    try:
        amount = float(input("Enter the amount to withdraw: $"))
        if amount <= user_account["balance"]:
            user_account["balance"] -= amount
        else:
                print("Insufficient funds.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def change_pin():
        new_pin = int(input("Enter your new 4-digit PIN: "))
        if 0000 <= new_pin <= 9999:
            user_account["pin"] = new_pin
            print("Your PIN has been successfully changed.")
        else:
            print("PIN must be a 4-digit number.")

def authentication():
        entered_pin = int(input("Enter your PIN: "))
        if entered_pin == user_account["pin"]:
            return True
        else:
            print("Incorrect PIN.")
            return False
        
def atm():
    print("Welcome to the ATM!")
    if not authentication():
        return

    while True:
        menu()
        try:
            choice = int(input("Select an option (1-5): "))
            if choice == 1:
                check_balance()
            elif choice == 2:
                deposit_money()
            elif choice == 3:
                withdraw_money()
            elif choice == 4:
                change_pin()
            elif choice == 5:
                print("Exit")
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid input")

atm()
