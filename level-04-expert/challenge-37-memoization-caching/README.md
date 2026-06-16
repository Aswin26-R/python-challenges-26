# Challenge 37: Memoization and Caching

**Level:** 4 – Expert Python
**Difficulty:** ⭐⭐⭐⭐ (Expert)
**Estimated Time:** 75 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- What memoization is and why it drastically improves performance
- How to build a manual cache with a dictionary
- How to use `functools.lru_cache` decorator
- How to implement a custom `Cache` class with LRU eviction
- Measuring and comparing performance with `time` module

---

## Problem Description

**Memoization** stores the results of expensive function calls. When the same inputs appear again, we return the cached result instead of recomputing. This can transform O(2^n) algorithms into O(n).

---

## Requirements

- [ ] `memoize(func)` — decorator that caches results by arguments
- [ ] `fibonacci_cached(n)` — Fibonacci using `@lru_cache` (compare to naive)
- [ ] `fibonacci_naive(n)` — Fibonacci without caching (for comparison)
- [ ] `Cache` class — simple LRU cache with max size, evicts oldest on overflow

---

## Expected Behavior

```python
# memoize decorator:
@memoize
def slow_add(a, b):
    return a + b

slow_add(1, 2)  # computed
slow_add(1, 2)  # returned from cache — no recomputation

# fibonacci_cached vs fibonacci_naive:
fibonacci_naive(35)    # slow — exponential time
fibonacci_cached(35)   # instant — cached!

# Cache class:
cache = Cache(max_size=3)
cache.set("a", 1)
cache.set("b", 2)
cache.set("c", 3)
cache.set("d", 4)  # "a" evicted — oldest entry

cache.get("a")     # None — was evicted
cache.get("b")     # 2
```

---

## Performance Comparison

```
fibonacci_naive(35)  → ~5 seconds
fibonacci_cached(35) → instant (cached after first call)
```

The difference is dramatic: naive Fibonacci has time complexity O(2^n) because it recomputes the same subproblems millions of times. With memoization, each value is computed exactly once: O(n).

---

## Hints

> **Hint 1:** `memoize` stores results in a dict: `cache = {}`. Key is `args` (a tuple, since dicts need hashable keys).

> **Hint 2:** In the wrapper: `if args in cache: return cache[args]`. Otherwise compute and store.

> **Hint 3:** For `fibonacci_cached`, just add `@functools.lru_cache(maxsize=None)` above `def fibonacci_cached(n)`.

> **Hint 4:** `Cache` class: use `self._store = {}` and `self._order = []`. On `set`, if key exists update it; if new and full, evict `_order[0]` (oldest).

---

## How to Run the Tests

```bash
cd level-04-expert/challenge-37-memoization-caching
pytest tests/ -v
```
