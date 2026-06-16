# Challenge 25: Regular Expressions

**Level:** 3 – Advanced Python
**Difficulty:** ⭐⭐⭐ (Advanced)
**Estimated Time:** 60 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to use Python's `re` module
- Basic regex patterns: `.`, `*`, `+`, `?`, `[]`, `^`, `$`, `\d`, `\w`
- How to search, match, and find all occurrences
- Practical use cases: validation, extraction, cleaning

---

## Problem Description

Regular expressions (regex) are patterns for matching text. They are used for validating email addresses, extracting data, finding and replacing text, and much more.

---

## Requirements

- [ ] `is_valid_email(email)` — returns `True` if email matches a basic email format
- [ ] `extract_numbers(text)` — returns a list of all numbers found in the text
- [ ] `is_valid_phone(phone)` — returns `True` if phone matches format: `+XX-XXX-XXX-XXXX`
- [ ] `replace_whitespace(text)` — replaces one or more consecutive spaces/tabs with a single space
- [ ] `extract_hashtags(text)` — returns a list of all hashtags from the text

---

## Expected Behavior

```python
is_valid_email("user@example.com")
# Returns: True

is_valid_email("not-an-email")
# Returns: False

is_valid_email("user@domain")
# Returns: False  (no dot after domain)

extract_numbers("I have 3 cats and 12 dogs worth $450")
# Returns: ["3", "12", "450"]

is_valid_phone("+91-987-654-3210")
# Returns: True

is_valid_phone("1234567890")
# Returns: False

replace_whitespace("hello   world\t\tpython")
# Returns: "hello world python"

extract_hashtags("I love #python and #coding is #fun")
# Returns: ["#python", "#coding", "#fun"]
```

---

## Quick Regex Reference

| Pattern | Matches |
|---------|---------|
| `\d` | Any digit (0-9) |
| `\w` | Any word character (a-z, A-Z, 0-9, _) |
| `\s` | Any whitespace (space, tab, newline) |
| `+` | One or more of the previous |
| `*` | Zero or more of the previous |
| `?` | Zero or one of the previous |
| `^` | Start of string |
| `$` | End of string |
| `[abc]` | Any of a, b, or c |
| `[^abc]` | Not a, b, or c |
| `.` | Any character except newline |

---

## re Module Functions

```python
import re

re.match(pattern, text)     # matches at the START of text
re.search(pattern, text)    # finds FIRST match anywhere
re.findall(pattern, text)   # returns LIST of all matches
re.sub(pattern, repl, text) # replace matches with repl
```

---

## Hints

> **Hint 1:** `is_valid_email`: pattern like `r'^[\w.+-]+@[\w-]+\.[\w.]+$'`

> **Hint 2:** `extract_numbers`: `re.findall(r'\d+', text)`

> **Hint 3:** `is_valid_phone`: pattern like `r'^\+\d{2}-\d{3}-\d{3}-\d{4}$'`

> **Hint 4:** `replace_whitespace`: `re.sub(r'[ \t]+', ' ', text)` — replace one or more spaces/tabs with one space.

> **Hint 5:** `extract_hashtags`: `re.findall(r'#\w+', text)`

---

## How to Run the Tests

```bash
cd level-03-advanced/challenge-25-regular-expressions
pytest tests/ -v
```
