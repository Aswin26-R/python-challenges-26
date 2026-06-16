# Challenge 27: Binary Search

**Level:** 3 – Advanced Python
**Difficulty:** ⭐⭐⭐ (Advanced)
**Estimated Time:** 55 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How binary search works and why it's efficient
- How to implement both iterative and recursive versions
- The concept of divide and conquer
- Algorithm complexity: O(log n) vs O(n) for linear search

---

## Problem Description

**Binary search** is an efficient algorithm for finding a value in a **sorted** list. Instead of checking every element, it cuts the search space in half each time.

With 1 million elements, linear search takes up to 1 million comparisons. Binary search takes at most 20.

---

## Requirements

- [ ] `binary_search_iterative(arr, target)` — returns the index of `target`, or `-1` if not found
- [ ] `binary_search_recursive(arr, target, low=0, high=None)` — same but using recursion
- [ ] `find_insert_position(arr, target)` — returns the index where `target` should be inserted to keep the list sorted

---

## Expected Behavior

```python
binary_search_iterative([1, 3, 5, 7, 9, 11], 7)
# Returns: 3  (index 3)

binary_search_iterative([1, 3, 5, 7, 9, 11], 4)
# Returns: -1  (4 not in the list)

binary_search_iterative([], 5)
# Returns: -1

binary_search_recursive([1, 3, 5, 7, 9, 11], 7)
# Returns: 3

find_insert_position([1, 3, 5, 7, 9], 4)
# Returns: 2  (4 should go between 3 and 5, at index 2)

find_insert_position([1, 3, 5, 7, 9], 0)
# Returns: 0  (0 goes before everything)

find_insert_position([1, 3, 5, 7, 9], 10)
# Returns: 5  (10 goes after everything)
```

---

## The Algorithm

```
sorted list: [1, 3, 5, 7, 9, 11]
looking for: 7

Step 1: low=0, high=5, mid=2 → arr[2]=5 < 7 → search right half
Step 2: low=3, high=5, mid=4 → arr[4]=9 > 7 → search left half
Step 3: low=3, high=3, mid=3 → arr[3]=7 == 7 → FOUND at index 3
```

---

## Hints

> **Hint 1:** `low` starts at 0, `high` starts at `len(arr) - 1`. Compute `mid = (low + high) // 2`.

> **Hint 2:** If `arr[mid] == target`: found, return `mid`.

> **Hint 3:** If `arr[mid] < target`: search right half → `low = mid + 1`.

> **Hint 4:** If `arr[mid] > target`: search left half → `high = mid - 1`.

> **Hint 5:** Stop when `low > high` — target not in list.

> **Hint 6:** For `find_insert_position`: run binary search but return `low` when target not found — that's where it would be inserted.

---

## How to Run the Tests

```bash
cd level-03-advanced/challenge-27-binary-search
pytest tests/ -v
```
