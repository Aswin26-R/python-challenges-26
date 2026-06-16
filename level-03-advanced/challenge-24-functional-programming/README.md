# Challenge 24: Functional Programming

**Level:** 3 – Advanced Python
**Difficulty:** ⭐⭐⭐ (Advanced)
**Estimated Time:** 55 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to use `map()`, `filter()`, and `reduce()`
- How to write `lambda` functions
- The functional programming paradigm: transforming data without loops
- How to chain functional operations

---

## Problem Description

Functional programming is a style where you transform data using functions rather than loops and mutations. Python has first-class support for functional programming through `map`, `filter`, `reduce`, and `lambda`.

---

## Requirements

- [ ] `apply_to_all(func, items)` — applies a function to every item in a list (using `map`)
- [ ] `keep_if(func, items)` — keeps only items for which `func` returns `True` (using `filter`)
- [ ] `reduce_list(func, items, initial)` — combines all items into one value (using `reduce`)
- [ ] `pipeline(value, *funcs)` — applies multiple functions in sequence to a value
- [ ] `compose(f, g)` — returns a new function that first applies `g`, then `f`

---

## Expected Behavior

```python
apply_to_all(lambda x: x * 2, [1, 2, 3, 4])
# Returns: [2, 4, 6, 8]

keep_if(lambda x: x > 3, [1, 2, 3, 4, 5, 6])
# Returns: [4, 5, 6]

reduce_list(lambda acc, x: acc + x, [1, 2, 3, 4, 5], 0)
# Returns: 15  (sum)

reduce_list(lambda acc, x: acc * x, [1, 2, 3, 4], 1)
# Returns: 24  (product)

pipeline(5, lambda x: x * 2, lambda x: x + 1, lambda x: x ** 2)
# Returns: 121  (5 → 10 → 11 → 121)

add_one = lambda x: x + 1
double = lambda x: x * 2
add_then_double = compose(double, add_one)
add_then_double(5)
# Returns: 12  (5 + 1 = 6, then 6 * 2 = 12)
```

---

## Lambda Functions

A `lambda` is a short, anonymous function:

```python
double = lambda x: x * 2
double(5)   # 10

# Same as:
def double(x):
    return x * 2
```

---

## map and filter

```python
# map: apply a function to every item
list(map(lambda x: x * 2, [1, 2, 3]))   # [2, 4, 6]

# filter: keep items where function returns True
list(filter(lambda x: x > 2, [1, 2, 3, 4]))   # [3, 4]
```

---

## Hints

> **Hint 1:** `apply_to_all`: use `list(map(func, items))`.

> **Hint 2:** `keep_if`: use `list(filter(func, items))`.

> **Hint 3:** `reduce_list`: use `from functools import reduce` then `reduce(func, items, initial)`.

> **Hint 4:** `pipeline`: start with `result = value`, then loop: `for func in funcs: result = func(result)`. Return result.

> **Hint 5:** `compose(f, g)`: return a lambda: `lambda x: f(g(x))`.

---

## How to Run the Tests

```bash
cd level-03-advanced/challenge-24-functional-programming
pytest tests/ -v
```
