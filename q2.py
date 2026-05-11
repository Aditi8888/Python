class Bank_Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero")
            return
        self.balance += amount
        print(f"₹{amount:.2f} deposited. New balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print(f"Insufficient funds. Your balance is only ₹{self.balance:.2f}")
            return
        self.balance -= amount
        print(f"₹{amount:.2f} withdrawn. New balance: ₹{self.balance:.2f}")

    def get_balance(self):
        print(f"Account owner  : {self.owner}")
        print(f"Current balance: ₹{self.balance:.2f}")
        return self.balance

acc = Bank_Account("Ravi", 1000)
acc.get_balance()
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)
acc.get_balance()