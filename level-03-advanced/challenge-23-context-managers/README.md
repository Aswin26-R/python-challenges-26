# Challenge 23: Context Managers

**Level:** 3 – Advanced Python
**Difficulty:** ⭐⭐⭐ (Advanced)
**Estimated Time:** 60 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- What context managers are and why they exist
- How to implement `__enter__` and `__exit__` methods
- How to use `contextlib.contextmanager` with `yield`
- Practical uses: resource cleanup, timing, temporary state

---

## Problem Description

A **context manager** is the mechanism behind Python's `with` statement. It ensures that setup and cleanup code always runs, even if an exception occurs.

```python
with open("file.txt") as f:   # f.__enter__() is called
    data = f.read()
# f.__exit__() is called automatically — file is closed
```

---

## Requirements

- [ ] `Timer` class — a context manager that measures time spent in the `with` block
- [ ] `managed_list()` — a generator-based context manager that creates a list and commits or discards changes
- [ ] `suppress_errors(*exception_types)` — a context manager that silently catches specified exceptions

---

## Expected Behavior

```python
with Timer() as t:
    time.sleep(0.1)
# After the block: t.elapsed is approximately 0.1

with Timer() as t:
    result = 2 + 2
print(f"Took {t.elapsed:.3f}s")

# managed_list:
with managed_list() as items:
    items.append(1)
    items.append(2)
# items is [1, 2] after the block (changes committed)

# suppress_errors:
with suppress_errors(ValueError):
    int("not_a_number")   # ValueError is suppressed
# code continues here normally

with suppress_errors(ValueError):
    raise TypeError("this is not suppressed")
# TypeError is NOT caught — it propagates
```

---

## Class-Based Context Manager

```python
class MyContext:
    def __enter__(self):
        # setup code runs here
        return self   # returned as the 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        # cleanup code runs here
        # return True to suppress exceptions
        # return False (or None) to let exceptions propagate
        return False
```

---

## Generator-Based Context Manager

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    # setup
    resource = create_something()
    try:
        yield resource        # the 'as' variable
    finally:
        cleanup(resource)     # always runs
```

---

## Hints

> **Hint 1:** `Timer`: store `time.time()` in `__enter__`, compute elapsed in `__exit__`, store as `self.elapsed`.

> **Hint 2:** `managed_list`: yield an empty list `[]`, then after yield the caller has modified it.

> **Hint 3:** `suppress_errors`: in `__exit__`, check `if exc_type is not None and issubclass(exc_type, exception_types): return True`. Returning `True` suppresses the exception.

---

## How to Run the Tests

```bash
cd level-03-advanced/challenge-23-context-managers
pytest tests/ -v
```
