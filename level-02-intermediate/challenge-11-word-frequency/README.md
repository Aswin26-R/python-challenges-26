# Challenge 11: Word Frequency

**Level:** 2 – Intermediate Python
**Difficulty:** ⭐⭐ (Intermediate)
**Estimated Time:** 35 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to split a string into words
- How to count items using a dictionary
- How to find the most common item
- How to ignore case when counting

---

## Problem Description

Counting word frequencies is a common real-world task used in text analysis, search engines, and data processing. You will write functions to count how often each word appears in a text.

---

## Requirements

- [ ] `count_words(text)` — returns a dictionary mapping each word to its count (case-insensitive)
- [ ] `most_common_word(text)` — returns the word that appears most often
- [ ] `unique_words(text)` — returns a sorted list of unique words (lowercase, no duplicates)

---

## Expected Behavior

```python
count_words("hello world hello")
# Returns: {"hello": 2, "world": 1}

count_words("The cat sat on the mat")
# Returns: {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}
# Note: "The" and "the" are counted as the same word

most_common_word("hello world hello python hello")
# Returns: "hello"

most_common_word("the cat sat on the mat")
# Returns: "the"

unique_words("banana apple banana cherry apple")
# Returns: ["apple", "banana", "cherry"]  (sorted, no duplicates)
```

---

## Counting with a Dictionary

The pattern for counting with a dictionary:

```python
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1   # word seen before, increment count
    else:
        counts[word] = 1    # word seen for first time, set to 1
```

Or using the `get()` method (more elegant):

```python
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
```

---

## Hints

> **Hint 1:** Convert text to lowercase first: `text.lower()` — ensures "The" and "the" are counted together.

> **Hint 2:** Split text into a list of words: `text.lower().split()`

> **Hint 3:** For `most_common_word()`, use `max(counts, key=counts.get)` to find the key with the highest value.

> **Hint 4:** For `unique_words()`, use `set()` to remove duplicates, then `sorted()` to sort.

---

## How to Run the Tests

```bash
cd level-02-intermediate/challenge-11-word-frequency
pytest tests/ -v
```
