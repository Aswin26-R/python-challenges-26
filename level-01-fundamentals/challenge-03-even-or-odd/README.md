# Challenge 03: Even or Odd

**Level:** 1 – Python Fundamentals
**Difficulty:** ⭐ (Beginner)
**Estimated Time:** 20 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to use `if` / `else` statements
- How to use the modulo operator (`%`)
- How to return different values based on conditions
- How to handle the edge case of zero

---

## Problem Description

A number is **even** if it can be divided by 2 with no remainder.
A number is **odd** if dividing by 2 leaves a remainder of 1.

You will write three functions that check and classify numbers.

---

## Requirements

- [ ] `is_even(number)` — returns `True` if the number is even, `False` if odd
- [ ] `is_odd(number)` — returns `True` if the number is odd, `False` if even
- [ ] `classify_number(number)` — returns the string `"even"` or `"odd"`

---

## The Modulo Operator

The `%` operator gives you the **remainder** of division:

```python
10 % 2  # = 0  (10 divided by 2, remainder 0 → even)
11 % 2  # = 1  (11 divided by 2, remainder 1 → odd)
7 % 2   # = 1  (7 divided by 2, remainder 1 → odd)
4 % 2   # = 0  (4 divided by 2, remainder 0 → even)
```

So to check if a number is even: `number % 2 == 0`

---

## Expected Behavior

```python
is_even(4)
# Returns: True

is_even(7)
# Returns: False

is_even(0)
# Returns: True  (zero is even!)

is_odd(3)
# Returns: True

is_odd(-4)
# Returns: False

classify_number(6)
# Returns: "even"

classify_number(9)
# Returns: "odd"

classify_number(-3)
# Returns: "odd"
```

---

## Edge Cases to Consider

- **Zero:** Is 0 even or odd? In mathematics, 0 is even because `0 % 2 == 0`.
- **Negative numbers:** `-4` is even, `-3` is odd. The modulo operator in Python handles negatives correctly.

---

## Hints

> **Hint 1:** To check if a number is even: `number % 2 == 0`

> **Hint 2:** If a number is even, then `is_odd()` is the opposite — not even.

> **Hint 3:** `classify_number()` should return the string `"even"` or `"odd"`, not `True`/`False`.

> **Hint 4:** For `is_odd()`, you can reuse your `is_even()` logic: a number is odd if it is NOT even.

---

## How to Run the Tests

```bash
cd level-01-fundamentals/challenge-03-even-or-odd
pytest tests/ -v
```
