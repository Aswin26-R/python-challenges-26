# Challenge 21: Decorators

**Level:** 3 – Advanced Python
**Difficulty:** ⭐⭐⭐ (Advanced)
**Estimated Time:** 60 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- What decorators are and how they modify functions
- How to write a decorator using closures
- How to use `functools.wraps` to preserve function metadata
- Practical use cases: timing, logging, validation

---

## Problem Description

A **decorator** is a function that wraps another function to add behavior before or after it runs — without changing the original function's code.

Decorators are used everywhere in Python frameworks (Django, Flask use `@login_required`, `@route`, etc.).

---

## Requirements

- [ ] `timer` decorator — measures and prints how long a function takes to run
- [ ] `logger` decorator — prints the function name, arguments, and return value
- [ ] `validate_positive` decorator — raises `ValueError` if any argument is not positive

---

## Expected Behavior

```python
@timer
def slow_function():
    import time
    time.sleep(0.1)
    return "done"

slow_function()
# Prints: "slow_function took 0.10 seconds"
# Returns: "done"

@logger
def add(a, b):
    return a + b

add(3, 4)
# Prints: "Calling add with args=(3, 4) kwargs={}"
# Prints: "add returned 7"
# Returns: 7

@validate_positive
def multiply(a, b):
    return a * b

multiply(3, 4)
# Returns: 12

multiply(-1, 4)
# Raises: ValueError("All arguments must be positive")
```

---

## How Decorators Work

```python
import functools

def my_decorator(func):
    @functools.wraps(func)      # preserves func's name and docstring
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        result = func(*args, **kwargs)  # call the original function
        print("After the function runs")
        return result
    return wrapper

@my_decorator
def greet(name):
    return f"Hello, {name}!"

# @my_decorator is the same as:
# greet = my_decorator(greet)
```

`*args` captures any positional arguments. `**kwargs` captures any keyword arguments.

---

## Hints

> **Hint 1:** All decorators follow the same structure: outer function takes `func`, inner function is `wrapper(*args, **kwargs)`, return `wrapper`.

> **Hint 2:** For `timer`, use `import time` and `time.time()` before and after calling `func(*args, **kwargs)`.

> **Hint 3:** For `logger`, use `func.__name__` to get the function name.

> **Hint 4:** For `validate_positive`, loop through `args` and check each one: `for arg in args: if arg <= 0: raise ValueError(...)`.

> **Hint 5:** Always use `@functools.wraps(func)` inside your decorator to preserve the wrapped function's metadata.

---

## How to Run the Tests

```bash
cd level-03-advanced/challenge-21-decorators
pytest tests/ -v
```
