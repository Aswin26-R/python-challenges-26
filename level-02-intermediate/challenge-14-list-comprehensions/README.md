# Challenge 14: List Comprehensions

**Level:** 2 – Intermediate Python
**Difficulty:** ⭐⭐ (Intermediate)
**Estimated Time:** 35 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- What list comprehensions are and why they are useful
- How to transform lists using comprehensions
- How to filter lists using comprehensions with conditions
- When to use comprehensions vs. regular loops

---

## Problem Description

List comprehensions are a powerful Python feature that let you create new lists in a single, readable line. They are faster than loops and considered more "Pythonic."

In this challenge, you must use list comprehensions — not regular for loops.

---

## The Syntax

```python
# Regular loop:
result = []
for x in items:
    result.append(x * 2)

# List comprehension (same result, one line):
result = [x * 2 for x in items]

# With a filter condition:
result = [x for x in items if x > 0]

# Transform AND filter:
result = [x * 2 for x in items if x > 0]
```

---

## Requirements

- [ ] `double_numbers(numbers)` — returns a new list with each number doubled
- [ ] `filter_evens(numbers)` — returns only the even numbers from the list
- [ ] `squares(numbers)` — returns a list of each number squared
- [ ] `filter_long_words(words, min_length)` — returns words longer than or equal to `min_length` characters
- [ ] `uppercase_words(words)` — returns a list of all words converted to uppercase

---

## Expected Behavior

```python
double_numbers([1, 2, 3, 4])
# Returns: [2, 4, 6, 8]

filter_evens([1, 2, 3, 4, 5, 6])
# Returns: [2, 4, 6]

squares([1, 2, 3, 4, 5])
# Returns: [1, 4, 9, 16, 25]

filter_long_words(["cat", "elephant", "dog", "butterfly"], 4)
# Returns: ["elephant", "butterfly"]

uppercase_words(["hello", "world", "python"])
# Returns: ["HELLO", "WORLD", "PYTHON"]
```

---

## Hints

> **Hint 1:** `double_numbers`: `[x * 2 for x in numbers]`

> **Hint 2:** `filter_evens`: `[x for x in numbers if x % 2 == 0]`

> **Hint 3:** `squares`: use `x ** 2` or `x * x` for squaring.

> **Hint 4:** `filter_long_words`: use `len(word) >= min_length` as the condition.

> **Hint 5:** `uppercase_words`: use `word.upper()` to convert each word.

---

## How to Run the Tests

```bash
cd level-02-intermediate/challenge-14-list-comprehensions
pytest tests/ -v
```
