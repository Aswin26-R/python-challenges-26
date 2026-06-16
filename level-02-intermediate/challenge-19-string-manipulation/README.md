# Challenge 19: String Manipulation

**Level:** 2 – Intermediate Python
**Difficulty:** ⭐⭐ (Intermediate)
**Estimated Time:** 40 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- A wide range of Python string methods
- How to clean, transform, and analyze strings
- String slicing and joining
- Building strings programmatically

---

## Problem Description

Strings are everywhere in software. User inputs need cleaning, text needs formatting, data needs parsing. This challenge gives you practice with Python's rich set of string methods.

---

## Requirements

- [ ] `title_case(text)` — converts text to Title Case (first letter of each word capitalized)
- [ ] `count_vowels(text)` — counts the number of vowels in the text (a, e, i, o, u)
- [ ] `remove_duplicates(text)` — removes consecutive duplicate characters
- [ ] `truncate(text, max_length)` — shortens text to max_length, adds "..." if truncated
- [ ] `is_anagram(word1, word2)` — returns True if the two words are anagrams of each other

---

## Expected Behavior

```python
title_case("hello world from python")
# Returns: "Hello World From Python"

count_vowels("Hello World")
# Returns: 3  (e, o, o)

count_vowels("rhythm")
# Returns: 0

remove_duplicates("aabbcc")
# Returns: "abc"

remove_duplicates("hello")
# Returns: "helo"  (ll becomes l)

truncate("Hello World", 8)
# Returns: "Hello..."  (first 5 chars + "...")

truncate("Hi", 10)
# Returns: "Hi"  (short enough, no truncation)

is_anagram("listen", "silent")
# Returns: True

is_anagram("hello", "world")
# Returns: False

is_anagram("Astronomer", "Moon starer")
# Returns: True  (case-insensitive, ignoring spaces)
```

---

## Useful String Methods

```python
"hello world".title()          # "Hello World"
"hello".upper()                # "HELLO"
"HELLO".lower()                # "hello"
"hello world".split()          # ["hello", "world"]
" ".join(["hello", "world"])   # "hello world"
"hello".count("l")             # 2
text.strip()                   # removes leading/trailing whitespace
```

---

## Hints

> **Hint 1:** `title_case()` — Python has a built-in `str.title()` method!

> **Hint 2:** `count_vowels()` — loop through the text and check `if char.lower() in "aeiou"`.

> **Hint 3:** `remove_duplicates()` — loop and only add a character if it differs from the previous one.

> **Hint 4:** `truncate()` — if `len(text) > max_length`: return `text[:max_length - 3] + "..."`. The `-3` leaves room for the three dots.

> **Hint 5:** `is_anagram()` — two words are anagrams if they have the same characters in any order. Hint: `sorted(word1.lower())` gives you the sorted characters.

---

## How to Run the Tests

```bash
cd level-02-intermediate/challenge-19-string-manipulation
pytest tests/ -v
```
