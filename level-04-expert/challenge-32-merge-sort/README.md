# Challenge 32: Merge Sort

**Level:** 4 – Expert Python
**Difficulty:** ⭐⭐⭐⭐ (Expert)
**Estimated Time:** 70 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- The Merge Sort algorithm — one of the most important sorting algorithms
- How divide-and-conquer recursion works at a deeper level
- Algorithm complexity: O(n log n) guaranteed performance
- How to merge two sorted arrays efficiently

---

## Problem Description

**Merge Sort** works by dividing the list in half repeatedly until each piece has only one element (a single element is always sorted), then merging those pieces back together in sorted order.

This is significantly faster than bubble sort for large lists — O(n log n) vs O(n²).

---

## Requirements

- [ ] `merge_sort(arr)` — returns a new sorted list using merge sort
- [ ] `merge(left, right)` — merges two sorted lists into one sorted list
- [ ] `merge_sort_inplace(arr)` — sorts the list in place (modifies original)

---

## Expected Behavior

```python
merge_sort([38, 27, 43, 3, 9, 82, 10])
# Returns: [3, 9, 10, 27, 38, 43, 82]

merge_sort([])
# Returns: []

merge_sort([1])
# Returns: [1]

merge([1, 3, 5], [2, 4, 6])
# Returns: [1, 2, 3, 4, 5, 6]

merge([1, 2, 3], [])
# Returns: [1, 2, 3]
```

---

## The Algorithm

```
merge_sort([38, 27, 43, 3]):

Step 1 — Divide:
  [38, 27, 43, 3]
  → [38, 27] and [43, 3]
  → [38] and [27] and [43] and [3]

Step 2 — Conquer (sort each piece):
  [38] and [27] → already sorted (size 1)
  [43] and [3] → already sorted (size 1)

Step 3 — Merge:
  merge([38], [27]) → [27, 38]
  merge([43], [3]) → [3, 43]
  merge([27, 38], [3, 43]) → [3, 27, 38, 43]
```

---

## The Merge Function

```python
def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both lists, take the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements (one list may finish before the other)
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

---

## Hints

> **Hint 1:** Base case: if `len(arr) <= 1`, return `arr` (already sorted).

> **Hint 2:** Find the midpoint: `mid = len(arr) // 2`.

> **Hint 3:** Recursively sort each half: `left = merge_sort(arr[:mid])`, `right = merge_sort(arr[mid:])`.

> **Hint 4:** Merge the two sorted halves: `return merge(left, right)`.

---

## How to Run the Tests

```bash
cd level-04-expert/challenge-32-merge-sort
pytest tests/ -v
```
