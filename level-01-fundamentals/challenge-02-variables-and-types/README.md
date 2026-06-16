# Challenge 02: Variables and Types

**Level:** 1 – Python Fundamentals
**Difficulty:** ⭐ (Beginner)
**Estimated Time:** 20 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- Python's four basic data types: `int`, `float`, `str`, `bool`
- How to use the `type()` function
- How to convert between types with `int()`, `float()`, `str()`
- How to check if a value is a specific type

---

## Problem Description

Every value in Python has a type. Understanding types is fundamental to writing correct programs. In this challenge, you will write functions that work with Python's basic types and demonstrate how to use them.

---

## Requirements

- [ ] `get_type_name(value)` — returns the type name of a value as a string (e.g. `"int"`, `"str"`)
- [ ] `is_integer(value)` — returns `True` if the value is an integer, `False` otherwise
- [ ] `is_string(value)` — returns `True` if the value is a string, `False` otherwise
- [ ] `convert_to_int(value)` — converts a value to an integer and returns it
- [ ] `convert_to_string(value)` — converts a value to a string and returns it
- [ ] `add_numbers(a, b)` — adds two numbers and returns the result

---

## Python's Basic Types

| Type | Description | Example |
|------|-------------|---------|
| `int` | Whole numbers | `42`, `-7`, `0` |
| `float` | Decimal numbers | `3.14`, `-0.5`, `2.0` |
| `str` | Text | `"hello"`, `"123"` |
| `bool` | True or False | `True`, `False` |

---

## Expected Behavior

```python
get_type_name(42)
# Returns: "int"

get_type_name(3.14)
# Returns: "float"

get_type_name("hello")
# Returns: "str"

get_type_name(True)
# Returns: "bool"

is_integer(5)
# Returns: True

is_integer("5")
# Returns: False

is_string("hello")
# Returns: True

convert_to_int("42")
# Returns: 42  (as an integer, not "42")

convert_to_string(99)
# Returns: "99"  (as a string, not 99)

add_numbers(3, 4)
# Returns: 7

add_numbers(1.5, 2.5)
# Returns: 4.0
```

---

## How to Get the Type Name

The `type()` function returns the type object. To get just the name as a string, use `type(value).__name__`:

```python
type(42).__name__      # Returns: "int"
type("hello").__name__ # Returns: "str"
type(3.14).__name__    # Returns: "float"
```

---

## Hints

> **Hint 1:** To check if something is an integer, use `isinstance(value, int)` which returns `True` or `False`.

> **Hint 2:** To convert a string to an integer, use `int("42")` → `42`.

> **Hint 3:** To convert a number to a string, use `str(99)` → `"99"`.

> **Hint 4:** `type(value).__name__` gives you the type name as a plain string.

---

## How to Run the Tests

```bash
cd level-01-fundamentals/challenge-02-variables-and-types
pytest tests/ -v
```
