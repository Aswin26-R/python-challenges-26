# Challenge 17: Classes and Objects

**Level:** 2 – Intermediate Python
**Difficulty:** ⭐⭐ (Intermediate)
**Estimated Time:** 45 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- What a class is and how to define one
- How to write an `__init__` method
- How to define and call instance methods
- How to use `self` to access instance attributes
- The basics of Object-Oriented Programming (OOP)

---

## Problem Description

A **class** is a blueprint for creating objects. An **object** is an instance of a class — a specific thing created from that blueprint.

You will build a `BankAccount` class that models a simple bank account with deposit and withdrawal functionality.

---

## Requirements

Create a class called `BankAccount` with:

- [ ] `__init__(self, owner, balance=0)` — initializes the account with owner name and starting balance
- [ ] `deposit(self, amount)` — adds amount to balance; raises `ValueError` if amount <= 0
- [ ] `withdraw(self, amount)` — subtracts amount from balance; raises `ValueError` if amount <= 0 or insufficient funds
- [ ] `get_balance(self)` — returns the current balance
- [ ] `__str__(self)` — returns a readable string like `"BankAccount(owner='Alice', balance=100.00)"`

---

## Expected Behavior

```python
account = BankAccount("Alice", 100)
account.get_balance()
# Returns: 100

account.deposit(50)
account.get_balance()
# Returns: 150

account.withdraw(30)
account.get_balance()
# Returns: 120

account.withdraw(200)
# Raises: ValueError("Insufficient funds")

account.deposit(-10)
# Raises: ValueError("Deposit amount must be positive")

str(account)
# Returns: "BankAccount(owner='Alice', balance=120.00)"
```

---

## How Classes Work

```python
class Dog:
    def __init__(self, name, breed):   # runs when object is created
        self.name = name               # self.name stores the name
        self.breed = breed

    def bark(self):                    # a method
        return f"{self.name} says: Woof!"

# Create an object (instance):
my_dog = Dog("Rex", "Labrador")
my_dog.bark()  # "Rex says: Woof!"
```

---

## Hints

> **Hint 1:** `self.balance` stores the balance. Set it in `__init__`: `self.balance = balance`.

> **Hint 2:** `deposit` should add to balance: `self.balance += amount`.

> **Hint 3:** `withdraw` needs two checks: amount > 0 AND amount <= current balance.

> **Hint 4:** `__str__` controls what `str(object)` and `print(object)` display.

---

## How to Run the Tests

```bash
cd level-02-intermediate/challenge-17-classes-and-objects
pytest tests/ -v
```
