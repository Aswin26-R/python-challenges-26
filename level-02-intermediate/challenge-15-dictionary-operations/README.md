# Challenge 15: Dictionary Operations

**Level:** 2 – Intermediate Python
**Difficulty:** ⭐⭐ (Intermediate)
**Estimated Time:** 40 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to create, read, update, and delete dictionary entries (CRUD)
- How to use dictionary methods: `.get()`, `.keys()`, `.values()`, `.items()`
- How to merge dictionaries
- How to iterate over a dictionary

---

## Problem Description

Dictionaries are Python's most versatile data structure. You will implement a set of functions that perform common dictionary operations used in real applications.

---

## Requirements

- [ ] `get_value(d, key, default=None)` — returns the value for `key`, or `default` if not found
- [ ] `add_or_update(d, key, value)` — adds or updates a key-value pair, returns the updated dict
- [ ] `remove_key(d, key)` — removes a key from the dict (if present), returns the updated dict
- [ ] `merge_dicts(d1, d2)` — merges two dicts (d2 values win on conflicts), returns new dict
- [ ] `invert_dict(d)` — swaps keys and values, returns new dict
- [ ] `get_all_keys(d)` — returns a sorted list of all keys

---

## Expected Behavior

```python
get_value({"a": 1, "b": 2}, "a")
# Returns: 1

get_value({"a": 1}, "z")
# Returns: None

get_value({"a": 1}, "z", "not found")
# Returns: "not found"

add_or_update({"a": 1}, "b", 2)
# Returns: {"a": 1, "b": 2}

add_or_update({"a": 1}, "a", 99)
# Returns: {"a": 99}  (updated existing key)

remove_key({"a": 1, "b": 2}, "a")
# Returns: {"b": 2}

remove_key({"a": 1}, "z")
# Returns: {"a": 1}  (key not found, unchanged)

merge_dicts({"a": 1, "b": 2}, {"b": 99, "c": 3})
# Returns: {"a": 1, "b": 99, "c": 3}  (d2 wins on conflict)

invert_dict({"a": 1, "b": 2, "c": 3})
# Returns: {1: "a", 2: "b", 3: "c"}

get_all_keys({"banana": 1, "apple": 2, "cherry": 3})
# Returns: ["apple", "banana", "cherry"]  (sorted)
```

---

## Hints

> **Hint 1:** `get_value()` — use `d.get(key, default)` which is built into Python.

> **Hint 2:** `merge_dicts()` — create a copy of d1, then update it with d2: `result = d1.copy(); result.update(d2)`.

> **Hint 3:** `invert_dict()` — use a dict comprehension: `{v: k for k, v in d.items()}`.

> **Hint 4:** `get_all_keys()` — use `sorted(d.keys())`.

---

## How to Run the Tests

```bash
cd level-02-intermediate/challenge-15-dictionary-operations
pytest tests/ -v
```
