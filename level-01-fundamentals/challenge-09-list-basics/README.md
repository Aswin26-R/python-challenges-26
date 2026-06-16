# Challenge 09: List Basics

**Level:** 1 – Python Fundamentals
**Difficulty:** ⭐⭐ (Beginner)
**Estimated Time:** 30 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to create and access items in a Python list
- Common list methods: `append()`, `remove()`, `sort()`, `reverse()`
- How to use `len()` to get a list's length
- How to get items by index (including negative indexes)

---

## Problem Description

Lists are one of Python's most important data structures. They store ordered collections of items. In this challenge, you will write functions that perform common list operations.

---

## Requirements

- [ ] `get_first(lst)` — returns the first item in the list (or `None` if empty)
- [ ] `get_last(lst)` — returns the last item in the list (or `None` if empty)
- [ ] `get_length(lst)` — returns the number of items in the list
- [ ] `add_item(lst, item)` — adds the item to the end of the list, returns the updated list
- [ ] `remove_item(lst, item)` — removes the first occurrence of item, returns the updated list (unchanged if item not found)
- [ ] `sort_list(lst)` — returns a new sorted list (do not modify the original)
- [ ] `sum_list(lst)` — returns the sum of all numbers in the list

---

## Expected Behavior

```python
get_first([10, 20, 30])
# Returns: 10

get_first([])
# Returns: None

get_last([10, 20, 30])
# Returns: 30

get_length([1, 2, 3, 4])
# Returns: 4

add_item([1, 2, 3], 4)
# Returns: [1, 2, 3, 4]

remove_item([1, 2, 3, 2], 2)
# Returns: [1, 3, 2]  (removes first occurrence only)

remove_item([1, 2, 3], 99)
# Returns: [1, 2, 3]  (99 not in list, return unchanged)

sort_list([3, 1, 2])
# Returns: [1, 2, 3]

sum_list([1, 2, 3, 4])
# Returns: 10
```

---

## List Indexing

```python
fruits = ["apple", "banana", "cherry"]
fruits[0]   # "apple"   — first item (index 0)
fruits[1]   # "banana"  — second item
fruits[-1]  # "cherry"  — last item (negative index!)
fruits[-2]  # "banana"  — second to last
```

---

## Common List Methods

```python
lst = [3, 1, 2]
lst.append(4)    # lst is now [3, 1, 2, 4]
lst.remove(1)    # lst is now [3, 2, 4]
lst.sort()       # lst is now [2, 3, 4]
len(lst)         # 3
sum(lst)         # 9
```

---

## Hints

> **Hint 1:** Check if a list is empty before accessing items: `if len(lst) == 0: return None`

> **Hint 2:** Last item shortcut: `lst[-1]` — negative indexes count from the end.

> **Hint 3:** For `sort_list()`, create a copy first to avoid modifying the original: `sorted_copy = lst.copy()` then sort it.

> **Hint 4:** For `remove_item()`, check if the item exists first: `if item in lst:` before calling `lst.remove(item)`.

---

## How to Run the Tests

```bash
cd level-01-fundamentals/challenge-09-list-basics
pytest tests/ -v
```
