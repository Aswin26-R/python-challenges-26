# Challenge 18: Recursion – Factorial

**Level:** 2 – Intermediate Python
**Difficulty:** ⭐⭐ (Intermediate)
**Estimated Time:** 40 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- What recursion is and how it works
- How to identify the base case and recursive case
- How to avoid infinite recursion
- How to implement both recursive and iterative solutions

---

## Problem Description

**Recursion** is when a function calls itself. It is a powerful technique for solving problems that can be broken into smaller versions of the same problem.

**Factorial** is the classic recursion example:
- `5! = 5 × 4 × 3 × 2 × 1 = 120`
- `5! = 5 × 4!`
- `4! = 4 × 3!`
- `3! = 3 × 2!`
- ... until we reach `1! = 1` (the base case)

---

## Requirements

- [ ] `factorial_recursive(n)` — compute factorial using recursion
- [ ] `factorial_iterative(n)` — compute factorial using a loop (no recursion)
- [ ] `count_down(n)` — returns a list counting down from n to 1 using recursion

---

## Expected Behavior

```python
factorial_recursive(5)
# Returns: 120  (5 × 4 × 3 × 2 × 1)

factorial_recursive(0)
# Returns: 1  (by mathematical definition, 0! = 1)

factorial_recursive(1)
# Returns: 1

factorial_iterative(5)
# Returns: 120

factorial_iterative(0)
# Returns: 1

count_down(5)
# Returns: [5, 4, 3, 2, 1]

count_down(1)
# Returns: [1]
```

---

## How Recursion Works

```python
def factorial_recursive(n):
    # Base case: stop condition
    if n == 0 or n == 1:
        return 1
    # Recursive case: call itself with a smaller problem
    return n * factorial_recursive(n - 1)

# How it executes for n=4:
# factorial_recursive(4)
#   = 4 * factorial_recursive(3)
#   = 4 * 3 * factorial_recursive(2)
#   = 4 * 3 * 2 * factorial_recursive(1)
#   = 4 * 3 * 2 * 1
#   = 24
```

**Two essential parts of recursion:**
1. **Base case** — when to stop (e.g., `n == 0`)
2. **Recursive case** — call yourself with a smaller input

Without a base case, recursion runs forever (stack overflow).

---

## Hints

> **Hint 1:** Base case for factorial: `if n == 0: return 1` (or `n <= 1`).

> **Hint 2:** Recursive case: `return n * factorial_recursive(n - 1)`.

> **Hint 3:** For `factorial_iterative()`, use a loop: `result = 1` then multiply each number from 1 to n.

> **Hint 4:** For `count_down()` recursion: base case is `n == 0`, return `[]`. Otherwise `[n] + count_down(n - 1)`.

---

## How to Run the Tests

```bash
cd level-02-intermediate/challenge-18-recursion-factorial
pytest tests/ -v
```
