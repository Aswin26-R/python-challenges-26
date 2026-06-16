# Challenge 04: Basic Calculator

**Level:** 1 – Python Fundamentals
**Difficulty:** ⭐ (Beginner)
**Estimated Time:** 25 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to write functions with multiple parameters
- Python's arithmetic operators: `+`, `-`, `*`, `/`
- How to handle division by zero
- How to return `None` for invalid operations

---

## Problem Description

You will build a set of calculator functions that perform basic arithmetic. A real calculator needs to handle edge cases gracefully — what happens if someone divides by zero?

---

## Requirements

- [ ] `add(a, b)` — returns the sum of `a` and `b`
- [ ] `subtract(a, b)` — returns `a` minus `b`
- [ ] `multiply(a, b)` — returns `a` times `b`
- [ ] `divide(a, b)` — returns `a` divided by `b`, or `None` if `b` is zero
- [ ] `calculate(a, operator, b)` — performs the operation specified by the `operator` string

---

## Python Arithmetic Operators

```python
5 + 3   # Addition:       8
5 - 3   # Subtraction:    2
5 * 3   # Multiplication: 15
5 / 3   # Division:       1.666...  (returns a float)
5 // 3  # Floor division: 1         (rounds down)
5 % 3   # Modulo:         2         (remainder)
```

---

## Expected Behavior

```python
add(3, 4)
# Returns: 7

subtract(10, 3)
# Returns: 7

multiply(4, 5)
# Returns: 20

divide(10, 2)
# Returns: 5.0

divide(10, 0)
# Returns: None  (cannot divide by zero!)

calculate(3, "+", 4)
# Returns: 7

calculate(10, "-", 3)
# Returns: 7

calculate(4, "*", 5)
# Returns: 20

calculate(10, "/", 2)
# Returns: 5.0

calculate(10, "/", 0)
# Returns: None
```

---

## The `calculate` Function

The `calculate` function takes three arguments:
- `a` — the first number
- `operator` — a string: `"+"`, `"-"`, `"*"`, or `"/"`
- `b` — the second number

Use `if/elif/else` to check which operator was given and call the correct function.

---

## Hints

> **Hint 1:** Division in Python uses `/` and always returns a float: `10 / 2` gives `5.0`, not `5`.

> **Hint 2:** To handle division by zero, check `if b == 0: return None` before dividing.

> **Hint 3:** For `calculate()`, compare the operator string: `if operator == "+":`

> **Hint 4:** What should `calculate()` return for an unknown operator like `"@"`? Return `None`.

---

## How to Run the Tests

```bash
cd level-01-fundamentals/challenge-04-basic-calculator
pytest tests/ -v
```
