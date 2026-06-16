# Challenge 12: Fibonacci Sequence

**Level:** 2 – Intermediate Python
**Difficulty:** ⭐⭐ (Intermediate)
**Estimated Time:** 30 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How the Fibonacci sequence works
- How to use a `while` or `for` loop to build sequences
- How to use variables to track previous values
- How to work with sequences and indices

---

## Problem Description

The Fibonacci sequence is one of the most famous mathematical sequences. Each number is the sum of the two numbers before it:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
```

Starting values: `0` and `1`

Rule: each next number = previous two numbers added together

---

## Requirements

- [ ] `fibonacci(n)` — returns the nth Fibonacci number (0-indexed)
- [ ] `fibonacci_sequence(count)` — returns a list of the first `count` Fibonacci numbers

---

## Expected Behavior

```python
fibonacci(0)
# Returns: 0  (the 0th Fibonacci number is 0)

fibonacci(1)
# Returns: 1

fibonacci(2)
# Returns: 1  (0 + 1 = 1)

fibonacci(7)
# Returns: 13  (sequence: 0,1,1,2,3,5,8,13 → 7th index = 13)

fibonacci_sequence(5)
# Returns: [0, 1, 1, 2, 3]

fibonacci_sequence(10)
# Returns: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

fibonacci_sequence(1)
# Returns: [0]

fibonacci_sequence(0)
# Returns: []
```

---

## The Algorithm

```python
# Building the sequence step by step:
a = 0   # first number
b = 1   # second number

# Each step: new number = a + b
# Then shift: a becomes b, b becomes the new number
step 1: next = 0 + 1 = 1, then a=1, b=1
step 2: next = 1 + 1 = 2, then a=1, b=2
step 3: next = 1 + 2 = 3, then a=2, b=3
step 4: next = 2 + 3 = 5, then a=3, b=5
```

---

## Hints

> **Hint 1:** Handle the base cases first: `fibonacci(0)` returns `0`, `fibonacci(1)` returns `1`.

> **Hint 2:** For `fibonacci(n)`, use a loop that runs `n-1` times, updating two variables each iteration.

> **Hint 3:** The classic swap pattern: `a, b = b, a + b` — Python evaluates the right side first, then assigns.

> **Hint 4:** For `fibonacci_sequence(count)`, build a list by appending each new number.

---

## How to Run the Tests

```bash
cd level-02-intermediate/challenge-12-fibonacci-sequence
pytest tests/ -v
```
