# Challenge 16: Exception Handling

**Level:** 2 – Intermediate Python
**Difficulty:** ⭐⭐ (Intermediate)
**Estimated Time:** 40 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- What exceptions are and why they happen
- How to use `try/except` to catch errors
- How to catch specific exception types
- How to use `finally` for cleanup code
- How to raise your own exceptions with `raise`

---

## Problem Description

Errors happen in real programs — users enter bad data, files don't exist, networks fail. Good code handles these situations gracefully instead of crashing. Python uses exceptions for error handling.

---

## Requirements

- [ ] `safe_divide(a, b)` — divides a by b, returns `None` if b is zero (no exception)
- [ ] `safe_int_convert(value)` — converts value to int, returns `None` if not possible
- [ ] `get_list_item(lst, index)` — gets item at index, returns `None` if index out of range
- [ ] `validate_age(age)` — raises `ValueError` with a message if age is not valid (must be 0–150)

---

## Expected Behavior

```python
safe_divide(10, 2)
# Returns: 5.0

safe_divide(10, 0)
# Returns: None  (no exception raised)

safe_int_convert("42")
# Returns: 42

safe_int_convert("hello")
# Returns: None  (can't convert "hello" to int)

safe_int_convert(3.7)
# Returns: 3

get_list_item([10, 20, 30], 1)
# Returns: 20

get_list_item([10, 20, 30], 99)
# Returns: None  (index 99 doesn't exist)

validate_age(25)
# Returns: True

validate_age(-1)
# Raises: ValueError("Age must be between 0 and 150")

validate_age(200)
# Raises: ValueError("Age must be between 0 and 150")
```

---

## How Try/Except Works

```python
try:
    result = 10 / 0     # This raises ZeroDivisionError
except ZeroDivisionError:
    result = None       # We catch it and handle it
```

Common exception types:
- `ZeroDivisionError` — dividing by zero
- `ValueError` — wrong type of value (e.g., `int("hello")`)
- `IndexError` — list index out of range
- `TypeError` — wrong type for an operation
- `FileNotFoundError` — file doesn't exist

---

## Raising Exceptions

You can raise your own exceptions to signal errors:

```python
def validate_positive(n):
    if n < 0:
        raise ValueError(f"{n} is negative — must be positive")
    return True
```

---

## Hints

> **Hint 1:** `safe_divide`: catch `ZeroDivisionError`.

> **Hint 2:** `safe_int_convert`: catch `ValueError` (for strings like "hello") and `TypeError`.

> **Hint 3:** `get_list_item`: catch `IndexError`.

> **Hint 4:** `validate_age`: use `if/raise`, not try/except. You are raising an error, not catching one.

---

## How to Run the Tests

```bash
cd level-02-intermediate/challenge-16-exception-handling
pytest tests/ -v
```
