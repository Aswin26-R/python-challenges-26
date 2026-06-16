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
        """
        TODO:
        Initialize the bank account.

        Parameters:
            owner   — the name of the account owner
            balance — starting balance (default is 0)

        Store these as instance attributes:
            self.owner = owner
            self.balance = balance
        """
        pass

    def deposit(self, amount):
        """
        TODO:
        Add the amount to the account balance.
        If amount is less than or equal to 0, raise a ValueError with the message:
        "Deposit amount must be positive"

        Examples:
            account = BankAccount("Alice", 100)
            account.deposit(50)    → balance is now 150
            account.deposit(0)     → raises ValueError("Deposit amount must be positive")
            account.deposit(-10)   → raises ValueError("Deposit amount must be positive")

        Hint:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
            self.balance += amount
        """
        pass

    def withdraw(self, amount):
        """
        TODO:
        Subtract the amount from the account balance.
        Raise ValueError if:
        - amount is less than or equal to 0: "Withdrawal amount must be positive"
        - amount is more than the current balance: "Insufficient funds"

        Examples:
            account = BankAccount("Alice", 100)
            account.withdraw(30)   → balance is now 70
            account.withdraw(200)  → raises ValueError("Insufficient funds")
            account.withdraw(-5)   → raises ValueError("Withdrawal amount must be positive")
        """
        pass

    def get_balance(self):
        """
        TODO:
        Return the current balance.

        Example:
            account = BankAccount("Alice", 100)
            account.get_balance()  → 100
        """
        pass

    def __str__(self):
        """
        TODO:
        Return a string representation of this bank account.

        Format: "BankAccount(owner='Alice', balance=100.00)"

        Note: The balance should be formatted with exactly 2 decimal places.

        Example:
            account = BankAccount("Alice", 150)
            str(account)  → "BankAccount(owner='Alice', balance=150.00)"

        Hint: Use an f-string:
            f"BankAccount(owner='{self.owner}', balance={self.balance:.2f})"
        """
        pass
