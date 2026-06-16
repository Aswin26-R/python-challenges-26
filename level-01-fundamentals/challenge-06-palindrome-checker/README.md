# Challenge 06: Palindrome Checker

**Level:** 1 – Python Fundamentals
**Difficulty:** ⭐ (Beginner)
**Estimated Time:** 25 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to compare strings
- How to use string methods: `.lower()`, `.replace()`
- How to clean input data before processing
- What it means for a string to be a palindrome

---

## Problem Description

A **palindrome** is a word or phrase that reads the same forwards and backwards.

Examples of palindromes:
- `"racecar"` → reversed: `"racecar"` ✓
- `"madam"` → reversed: `"madam"` ✓
- `"A man a plan a canal Panama"` → ignoring spaces and case: palindrome ✓

You will write functions to check whether a string is a palindrome.

---

## Requirements

- [ ] `is_palindrome(text)` — returns `True` if `text` is a palindrome (case-insensitive, ignores spaces)
- [ ] `clean_string(text)` — returns the text in lowercase with all spaces removed

---

## Expected Behavior

```python
clean_string("Hello World")
# Returns: "helloworld"

clean_string("Race Car")
# Returns: "racecar"

is_palindrome("racecar")
# Returns: True

is_palindrome("hello")
# Returns: False

is_palindrome("Madam")
# Returns: True  (case-insensitive: "madam" == "madam" reversed)

is_palindrome("A man a plan a canal Panama")
# Returns: True  (ignore spaces and case)

is_palindrome("")
# Returns: True  (empty string is a palindrome)

is_palindrome("a")
# Returns: True  (single character is always a palindrome)
```

---

## Approach

The easiest way to check for a palindrome:
1. Clean the string (lowercase, remove spaces)
2. Compare the cleaned string to its reverse
3. If they are equal, it's a palindrome

```python
cleaned = clean_string(text)
return cleaned == cleaned[::-1]
```

---

## Hints

> **Hint 1:** Convert to lowercase with `text.lower()` — this makes `"Madam"` and `"madam"` compare as equal.

> **Hint 2:** Remove spaces with `text.replace(" ", "")` — this replaces every space with nothing.

> **Hint 3:** Reverse a string with `text[::-1]`.

> **Hint 4:** `clean_string()` should do both steps: lowercase AND remove spaces.

> **Hint 5:** `is_palindrome()` can use `clean_string()` inside it.

---

## How to Run the Tests

```bash
cd level-01-fundamentals/challenge-06-palindrome-checker
pytest tests/ -v
```
