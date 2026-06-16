# Challenge 13: Prime Number Checker

**Level:** 2 – Intermediate Python
**Difficulty:** ⭐⭐ (Intermediate)
**Estimated Time:** 35 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- What prime numbers are and how to detect them
- How to use nested loops efficiently
- How to use `break` and `return` early to exit loops
- How to optimize using the square root trick

---

## Problem Description

A **prime number** is a number greater than 1 that has no divisors other than 1 and itself.

Examples:
- `2` — prime (divisible only by 1 and 2)
- `3` — prime
- `4` — NOT prime (divisible by 2)
- `17` — prime
- `100` — NOT prime (divisible by 2, 4, 5, 10, 20, 25, 50)

---

## Requirements

- [ ] `is_prime(n)` — returns `True` if `n` is prime, `False` otherwise
- [ ] `get_primes(limit)` — returns a list of all prime numbers up to and including `limit`

---

## Expected Behavior

```python
is_prime(2)
# Returns: True

is_prime(3)
# Returns: True

is_prime(4)
# Returns: False

is_prime(17)
# Returns: True

is_prime(1)
# Returns: False  (1 is NOT prime by definition)

is_prime(0)
# Returns: False

is_prime(-5)
# Returns: False

get_primes(10)
# Returns: [2, 3, 5, 7]

get_primes(20)
# Returns: [2, 3, 5, 7, 11, 13, 17, 19]

get_primes(2)
# Returns: [2]
```

---

## The Algorithm

Basic approach:
1. If `n < 2`, return `False` immediately
2. Try to divide `n` by every number from `2` to `n-1`
3. If any division has no remainder (`n % i == 0`), it's NOT prime
4. If no divisor found, it IS prime

**Optimization:** You only need to check up to the square root of `n`. If `n` has a factor larger than its square root, then it also has a factor smaller than its square root.

```python
import math
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        return False
return True
```

---

## Hints

> **Hint 1:** Numbers less than 2 are never prime. Handle this first: `if n < 2: return False`.

> **Hint 2:** 2 is the only even prime number. All other even numbers are not prime.

> **Hint 3:** For `get_primes()`, use a loop and call your `is_prime()` function for each number.

> **Hint 4:** `import math` at the top of your file to use `math.sqrt()`.

---

## How to Run the Tests

```bash
cd level-02-intermediate/challenge-13-prime-checker
pytest tests/ -v
```
