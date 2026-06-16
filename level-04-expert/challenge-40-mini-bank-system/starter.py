import uuid


# ─────────────────────────────────────────
# Custom Exceptions
# ─────────────────────────────────────────

class InsufficientFundsError(Exception):
    """
    TODO:
    Raised when a withdrawal amount exceeds available balance (including overdraft).
    This class just needs to exist — no extra methods needed.
    Python's built-in Exception provides everything.
    """
    pass


class AccountNotFoundError(Exception):
    """
    TODO:
    Raised when trying to access an account ID that doesn't exist in the bank.
    """
    pass


class InvalidAmountError(Exception):
    """
    TODO:
    Raised when an amount is zero or negative (invalid for deposits/withdrawals).
    """
    pass


# ─────────────────────────────────────────
# Account Base Class
# ─────────────────────────────────────────

class Account:
    """
    TODO:
    Base class for all bank accounts.

    Attributes:
        account_id  — unique string ID (use str(uuid.uuid4())[:8])
        owner       — owner's name
        _balance    — current balance (float), starts at 0.0
        _history    — list of transaction dicts

    Transaction dict format:
        {"type": "deposit", "amount": 500.0, "balance_after": 500.0}
        {"type": "withdrawal", "amount": 200.0, "balance_after": 300.0}
    """

    def __init__(self, owner, balance=0.0):
        """
        TODO:
        Initialize the account:
            self.account_id = str(uuid.uuid4())[:8]
            self.owner = owner
            self._balance = float(balance)
            self._history = []
        """
        pass

    def deposit(self, amount):
        """
        TODO:
        Add amount to balance.
        Raise InvalidAmountError if amount <= 0.
        Record transaction in history.
        Return new balance.

        Example:
            account.deposit(500)   → balance becomes 500.0
            account.deposit(-10)   → raises InvalidAmountError
        """
        pass

    def withdraw(self, amount):
        """
        TODO:
        Subtract amount from balance.
        Raise InvalidAmountError if amount <= 0.
        Raise InsufficientFundsError if amount > self._balance.
        Record transaction in history.
        Return new balance.
        """
        pass

    def get_balance(self):
        """
        TODO:
        Return current balance.
        """
        pass

    def get_history(self):
        """
        TODO:
        Return the transaction history list.
        """
        pass

    def _record(self, transaction_type, amount):
        """
        TODO:
        Append a transaction dict to self._history.
        Format: {"type": transaction_type, "amount": amount, "balance_after": self._balance}
        """
        pass

    def __str__(self):
        """
        TODO:
        Return a string like:
        "Account(id='abc12345', owner='Alice', balance=500.00)"
        """
        pass


# ─────────────────────────────────────────
# SavingsAccount
# ─────────────────────────────────────────

class SavingsAccount(Account):
    """
    TODO:
    A savings account that earns interest.

    Additional attribute:
        interest_rate — default 0.05 (5%)

    Additional method:
        apply_interest() — multiply balance by (1 + interest_rate)
                           record as transaction type "interest"
                           return new balance

    Example:
        acc = SavingsAccount("Alice", interest_rate=0.1)
        acc.deposit(1000)
        acc.apply_interest()   → balance becomes 1100.0
    """

    def __init__(self, owner, balance=0.0, interest_rate=0.05):
        """
        TODO:
        Call super().__init__(owner, balance) then store interest_rate.
        """
        pass

    def apply_interest(self):
        """
        TODO:
        Multiply balance by (1 + interest_rate).
        Record transaction: {"type": "interest", "amount": interest_earned, "balance_after": ...}
        Return new balance.

        interest_earned = self._balance * self.interest_rate
        self._balance += interest_earned
        self._record("interest", interest_earned)
        return self._balance
        """
        pass


# ─────────────────────────────────────────
# CheckingAccount
# ─────────────────────────────────────────

class CheckingAccount(Account):
    """
    TODO:
    A checking account with overdraft protection.

    Additional attribute:
        overdraft_limit — default 100.0 (can go up to -100.0)

    Override withdraw():
        Allow balance to go negative, but not below -overdraft_limit.
        Raise InsufficientFundsError if amount > self._balance + self.overdraft_limit.

    Example:
        acc = CheckingAccount("Bob", overdraft_limit=100)
        acc.deposit(50)
        acc.withdraw(100)   → balance = -50.0  (OK, within overdraft)
        acc.withdraw(100)   → raises InsufficientFundsError (would go to -150, beyond -100 limit)
    """

    def __init__(self, owner, balance=0.0, overdraft_limit=100.0):
        """
        TODO:
        Call super().__init__(owner, balance) then store overdraft_limit.
        """
        pass

    def withdraw(self, amount):
        """
        TODO:
        Override withdraw to allow overdraft.

        Raise InvalidAmountError if amount <= 0.
        Raise InsufficientFundsError if amount > self._balance + self.overdraft_limit.
        Otherwise subtract amount, record, return balance.

        Check: if amount > self._balance + self.overdraft_limit: raise InsufficientFundsError
        """
        pass


# ─────────────────────────────────────────
# Bank
# ─────────────────────────────────────────

class Bank:
    """
    TODO:
    Manages a collection of accounts.

    Attribute:
        self._accounts = {}  ← {account_id: Account object}
    """

    def __init__(self):
        """
        TODO:
        Initialize with empty accounts dict.
        """
        pass

    def create_account(self, owner, account_type="checking", **kwargs):
        """
        TODO:
        Create a new account and store it in self._accounts.
        Return the new account object.

        account_type="checking" → create CheckingAccount(owner, **kwargs)
        account_type="savings"  → create SavingsAccount(owner, **kwargs)

        Hint:
            if account_type == "savings":
                account = SavingsAccount(owner, **kwargs)
            else:
                account = CheckingAccount(owner, **kwargs)
            self._accounts[account.account_id] = account
            return account
        """
        pass

    def get_account(self, account_id):
        """
        TODO:
        Return the Account object for account_id.
        Raise AccountNotFoundError if not found.
        """
        pass

    def deposit(self, account_id, amount):
        """
        TODO:
        Deposit into account. Return new balance.
        """
        pass

    def withdraw(self, account_id, amount):
        """
        TODO:
        Withdraw from account. Return new balance.
        """
        pass

    def transfer(self, from_id, to_id, amount):
        """
        TODO:
        Transfer amount from one account to another.
        The withdrawal should happen first; if it fails, don't deposit.
        Return True on success.

        Hint:
            from_acc = self.get_account(from_id)
            to_acc = self.get_account(to_id)
            from_acc.withdraw(amount)   ← raises if insufficient
            to_acc.deposit(amount)      ← only runs if withdraw succeeded
            return True
        """
        pass

    def get_balance(self, account_id):
        """
        TODO:
        Return balance for account_id.
        """
        pass

    def total_assets(self):
        """
        TODO:
        Return sum of all account balances.
        """
        pass
