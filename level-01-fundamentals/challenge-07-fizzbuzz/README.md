# Challenge 07: FizzBuzz

**Level:** 1 – Python Fundamentals
**Difficulty:** ⭐ (Beginner)
**Estimated Time:** 25 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to write `for` loops in Python
- How to use multiple `if/elif/else` conditions
- The importance of condition order
- How to build and return a list

---   

## Problem Description

FizzBuzz is one of the most famous beginner programming challenges. It tests your ability to write loops and conditions correctly.

The rules are simple:
- For numbers divisible by **3**: return/print `"Fizz"`
- For numbers divisible by **5**: return/print `"Buzz"`
- For numbers divisible by **both 3 and 5**: return/print `"FizzBuzz"`
- For all other numbers: return/print the number itself as a string

---

## Requirements

- [ ] `fizzbuzz(n)` — given a single number, returns the correct FizzBuzz string for it
- [ ] `fizzbuzz_list(start, end)` — returns a list of FizzBuzz results for all numbers from `start` to `end` (inclusive)

---

## Expected Behavior

```python
fizzbuzz(1)
# Returns: "1"

fizzbuzz(3)
# Returns: "Fizz"

fizzbuzz(5)
# Returns: "Buzz"

fizzbuzz(15)
# Returns: "FizzBuzz"

fizzbuzz(7)
# Returns: "7"

fizzbuzz_list(1, 5)
# Returns: ["1", "2", "Fizz", "4", "Buzz"]

fizzbuzz_list(13, 16)
# Returns: ["13", "14", "FizzBuzz", "16"]
```

---

## The Order of Conditions Matters!

This is the most important part of FizzBuzz. You must check for `FizzBuzz` (divisible by both 3 and 5) BEFORE checking for `Fizz` or `Buzz` alone.

```python
# WRONG ORDER:
if n % 3 == 0:
    return "Fizz"      # 15 hits this and returns "Fizz" — incorrect!
elif n % 5 == 0:
    return "Buzz"
elif n % 3 == 0 and n % 5 == 0:
    return "FizzBuzz"  # This is never reached for 15!

# CORRECT ORDER:
if n % 3 == 0 and n % 5 == 0:
    return "FizzBuzz"  # Check the most specific case FIRST
elif n % 3 == 0:
    return "Fizz"
elif n % 5 == 0:
    return "Buzz"
```

---

## Hints

> **Hint 1:** Check for divisibility by both 3 AND 5 first. If you check 3 first, 15 would return "Fizz" instead of "FizzBuzz".

> **Hint 2:** `range(start, end + 1)` gives you numbers from `start` to `end` inclusive. Without `+ 1`, the last number is excluded.

> **Hint 3:** For `fizzbuzz_list()`, create an empty list `result = []`, then use a for loop and `result.append(fizzbuzz(n))`.

> **Hint 4:** Numbers that are not Fizz, Buzz, or FizzBuzz should be returned as strings: `str(n)`, not the integer `n`.

---

## How to Run the Tests

```bash
cd level-01-fundamentals/challenge-07-fizzbuzz
pytest tests/ -v
```
