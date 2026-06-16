# Challenge 40: Mini Bank System

**Level:** 4 – Expert Python
**Difficulty:** ⭐⭐⭐⭐⭐ (Expert — Capstone)
**Estimated Time:** 120 minutes

---

## Learning Objectives

This is the **capstone challenge** — it brings together everything you've learned:

- Object-Oriented Programming (classes, inheritance, encapsulation)
- Exception handling (custom exceptions)
- Data persistence (JSON file)
- Python built-ins (dataclasses, typing, datetime)
- Unit testing with pytest

---

## Problem Description

Build a simplified bank system with multiple account types, transaction history, and proper error handling. This is a real-world style project that exercises design thinking, not just syntax.

---

## Requirements

### Custom Exceptions
- `InsufficientFundsError(Exception)` — raised when withdrawal exceeds balance
- `AccountNotFoundError(Exception)` — raised when account ID doesn't exist
- `InvalidAmountError(Exception)` — raised for zero or negative amounts

### Account Classes

**`Account` (base class)**
- `__init__(account_id, owner, balance=0.0)`
- `deposit(amount)` — add funds (raises `InvalidAmountError` if amount <= 0)
- `withdraw(amount)` — subtract funds (raises `InsufficientFundsError` if insufficient, `InvalidAmountError` if <= 0)
- `get_balance()` — return current balance
- `get_history()` — return list of transaction records
- `__str__` — human-readable representation

**`SavingsAccount(Account)`**
- Adds `interest_rate` (default 0.05 = 5%)
- `apply_interest()` — multiply balance by (1 + interest_rate) and record as a transaction

**`CheckingAccount(Account)`**
- Adds `overdraft_limit` (default 100.0)
- `withdraw(amount)` — allows going negative, down to -overdraft_limit
- Raises `InsufficientFundsError` if withdrawal would exceed overdraft

### Bank Class
- `__init__()` — initialize with empty accounts dict
- `create_account(owner, account_type="checking", **kwargs)` — create and store account, return account object
- `get_account(account_id)` — return account by ID (raises `AccountNotFoundError`)
- `deposit(account_id, amount)` — deposit to account
- `withdraw(account_id, amount)` — withdraw from account
- `transfer(from_id, to_id, amount)` — transfer between accounts
- `get_balance(account_id)` — return account balance
- `total_assets()` — sum of all account balances

---

## Expected Behavior

```python
bank = Bank()

# Create accounts:
checking = bank.create_account("Alice", "checking")
savings  = bank.create_account("Bob", "savings", interest_rate=0.1)

# Deposit and withdraw:
bank.deposit(checking.account_id, 1000)
bank.withdraw(checking.account_id, 200)
bank.get_balance(checking.account_id)   # 800.0

# Transfer:
bank.transfer(checking.account_id, savings.account_id, 100)

# Savings interest:
bank.deposit(savings.account_id, 500)
savings.apply_interest()
bank.get_balance(savings.account_id)   # 550.0 + transfer = 650.0

# Error handling:
bank.withdraw(checking.account_id, 99999)  # raises InsufficientFundsError
bank.get_account("fake-id")               # raises AccountNotFoundError
bank.deposit(checking.account_id, -50)    # raises InvalidAmountError

# Overdraft (CheckingAccount only):
bank.withdraw(checking.account_id, 800)   # balance goes to 0, then -100 is limit
```

---

## Transaction History Format

```python
account.get_history()
# Returns list of dicts:
[
    {"type": "deposit",    "amount": 1000.0, "balance_after": 1000.0},
    {"type": "withdrawal", "amount": 200.0,  "balance_after": 800.0},
    {"type": "transfer",   "amount": 100.0,  "balance_after": 700.0},
]
```

---

## Hints

> **Hint 1:** Generate unique account IDs using `str(uuid.uuid4())[:8]` or a simple counter.

> **Hint 2:** Track transaction history as `self._history = []`. Each transaction is a dict.

> **Hint 3:** `CheckingAccount.withdraw` should check: if `amount > self._balance + self.overdraft_limit` → raise `InsufficientFundsError`.

> **Hint 4:** `Bank.transfer` should be atomic: deposit fails? don't withdraw. Use try/except to ensure both succeed or neither does.

---

## How to Run the Tests

```bash
cd level-04-expert/challenge-40-mini-bank-system
pytest tests/ -v
```

**Congratulations on reaching the final challenge! This is the most complete exercise in the repository — take your time and design it well.**
