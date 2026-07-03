class BankAccount:
    """
    TODO:
    A class representing a simple bank account.

    Attributes:
        owner   — the name of the account owner (string)
        balance — the current account balance (number, default 0)

    Methods:
        deposit(amount)  — add money to the account
        withdraw(amount) — remove money from the account
        get_balance()    — return the current balance
        __str__()        — return a readable string representation
    """

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        pass

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        pass

    def get_balance(self):
        return self.balance

        pass

    def __str__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance:.2f})"
        pass
