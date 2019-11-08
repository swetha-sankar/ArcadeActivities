# Bank accounts have a name and a balance
class BankAccount:
    name: str
    balance: int

    def __init__(self, account_name: str, initial_balance: int):
        self.name = account_name
        self.balance = initial_balance

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount:int):
        if amount > self.balance:
            old_balance = self.balance
            self.balance = 0
            return old_balance
        else:
            self.balance -= amount
            return amount


swetha_points = BankAccount("UD points", 100)
lauren_points = BankAccount("UD points", 20)

swetha_points.deposit(200)
print("You have", swetha_points.balance, "dollars")

# SafeAccount - cannot be overdrawn
