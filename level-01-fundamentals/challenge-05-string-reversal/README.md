# Challenge 05: String Reversal

**Level:** 1 – Python Fundamentals
**Difficulty:** ⭐ (Beginner)
**Estimated Time:** 20 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to slice strings in Python
- The `[::-1]` reverse slice syntax
- How to split a string into words and rejoin them
- How to handle empty strings

---

## Problem Description

Reversing strings is a classic programming task that teaches you about string indexing and slicing. You will write two functions: one to reverse the characters in a string, and one to reverse the order of words in a sentence.

---

## Requirements

- [ ] `reverse_string(text)` — returns the string with characters in reverse order
- [ ] `reverse_words(sentence)` — returns the sentence with words in reverse order

---

## String Slicing

In Python, you can slice (cut out a piece of) a string using `[start:stop:step]`:

```python
text = "hello"
text[0]     # "h"   — first character
text[-1]    # "o"   — last character
text[1:3]   # "el"  — characters at index 1 and 2
text[::-1]  # "olleh" — reverse: step of -1 goes backwards
```

The `[::-1]` slice is the standard Python way to reverse a string.

---

## Expected Behavior

```python
reverse_string("hello")
# Returns: "olleh"

reverse_string("Python")
# Returns: "nohtyP"

reverse_string("")
# Returns: ""  (empty string reversed is still empty)

reverse_string("a")
# Returns: "a"  (single character is the same reversed)

reverse_words("hello world")
# Returns: "world hello"

reverse_words("I love Python")
# Returns: "Python love I"

reverse_words("one")
# Returns: "one"  (single word stays the same)
```

---

## Hints

> **Hint 1:** To reverse a string: `text[::-1]` — this is the most Pythonic way.

> **Hint 2:** To split a string into a list of words: `sentence.split()` — this splits on spaces.

> **Hint 3:** To join a list of words back into a string: `" ".join(words_list)`

> **Hint 4:** Combining split, reverse, and join:
> ```python
> words = sentence.split()    # ["hello", "world"]
> words.reverse()             # ["world", "hello"]
> result = " ".join(words)   # "world hello"
> ```

---

## How to Run the Tests

```bash
cd level-01-fundamentals/challenge-05-string-reversal
pytest tests/ -v
```
