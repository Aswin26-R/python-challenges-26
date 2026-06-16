# Challenge 22: Generators

**Level:** 3 – Advanced Python
**Difficulty:** ⭐⭐⭐ (Advanced)
**Estimated Time:** 60 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- What generators are and why they use less memory than lists
- How to use the `yield` keyword
- The difference between a generator and a regular function
- How to use `next()` and iterate over generators

---

## Problem Description

A **generator** is a special kind of function that produces values one at a time using the `yield` keyword. Unlike a list (which stores all values in memory at once), a generator only computes the next value when asked.

This makes generators ideal for large sequences — you can generate a billion numbers without storing a billion numbers in memory.

---

## Requirements

- [ ] `count_up(start, end)` — generator that yields integers from `start` to `end`
- [ ] `fibonacci_generator()` — infinite generator that yields Fibonacci numbers forever
- [ ] `take(generator, n)` — returns the first `n` values from a generator as a list
- [ ] `squares_generator(limit)` — generator that yields squares: 1, 4, 9, 16, ... up to limit

---

## Expected Behavior

```python
gen = count_up(1, 5)
list(gen)
# Returns: [1, 2, 3, 4, 5]

next(count_up(10, 12))
# Returns: 10

fib = fibonacci_generator()
take(fib, 8)
# Returns: [0, 1, 1, 2, 3, 5, 8, 13]

squares = squares_generator(30)
list(squares)
# Returns: [1, 4, 9, 16, 25]  (squares up to 30)

take(count_up(1, 100), 3)
# Returns: [1, 2, 3]
```

---

## How Generators Work

```python
def countdown(n):
    while n > 0:
        yield n       # pause and return this value
        n -= 1        # resume here on next() call

gen = countdown(3)
next(gen)   # 3
next(gen)   # 2
next(gen)   # 1
next(gen)   # raises StopIteration (no more values)

# Or loop over it:
for value in countdown(3):
    print(value)   # 3, 2, 1
```

**Key points:**
- `yield` pauses the function and returns the value
- The function resumes from where it left off on the next `next()` call
- When the function returns (or runs out of code), `StopIteration` is raised

---

## Hints

> **Hint 1:** `count_up`: use a `for` loop with `yield` inside it.

> **Hint 2:** `fibonacci_generator`: use an infinite `while True` loop, yielding each value and updating `a, b = b, a + b`.

> **Hint 3:** `take(generator, n)`: use a list comprehension or loop to get the first n values: `[next(generator) for _ in range(n)]`.

> **Hint 4:** `squares_generator`: generate `i*i` for i starting at 1, and stop when `i*i > limit`.

---

## How to Run the Tests

```bash
cd level-03-advanced/challenge-22-generators
pytest tests/ -v
```
