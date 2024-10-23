class BankAccount:
    def __init__(self, ibalance=0):
        self.balance = ibalance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        elif amount > self.balance:
            print("Insufficient funds.")
    def check_balance(self):
        return self.balance




from bank_account import BankAccount
account = BankAccount(300)
account.deposit(50)
account.withdraw(40)
account.withdraw(100)
current_balance = account.check_balance()
print(f"Current balance: ${current_balance}")
