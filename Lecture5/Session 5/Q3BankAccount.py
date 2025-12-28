class BankAccount:

    # Constructor (Data Member)
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Deposit Function
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited(yani ki zama karna ): ₹{amount}")

    # Withdraw Function
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn(nikalna): ₹{amount}")
        else:
            print("Insufficient Balance!")

    # Check Balance Function
    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")


# Create Object
account = BankAccount("Aamir", 1000)

# Perform Operations
account.check_balance()
account.deposit(500)
account.withdraw(300)
account.check_balance()
