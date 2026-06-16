# Challenge 31: Singleton Pattern

**Level:** 4 – Expert Python
**Difficulty:** ⭐⭐⭐⭐ (Expert)
**Estimated Time:** 75 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- The Singleton design pattern and when to use it
- How to control class instantiation with `__new__`
- Thread-safe singleton implementation
- When singletons are appropriate and when to avoid them

---

## Problem Description

The **Singleton** pattern ensures that a class has only one instance. Every call to create the class returns the same object. This is useful for shared resources like configuration, logging, or database connections.

---

## Requirements

- [ ] `Singleton` base class — ensures only one instance can be created
- [ ] `AppConfig` class (extends Singleton) — stores app-wide configuration
- [ ] `Logger` class (extends Singleton) — tracks log messages

---

## Expected Behavior

```python
# Two calls return THE SAME object:
s1 = Singleton()
s2 = Singleton()
s1 is s2   # True — same object!

# AppConfig retains state across instances:
config1 = AppConfig()
config1.set("debug", True)

config2 = AppConfig()
config2.get("debug")   # True — same instance, same data

# Logger accumulates messages:
log1 = Logger()
log1.log("App started")

log2 = Logger()
log2.get_logs()   # ["App started"] — same instance
```

---

## The Singleton Implementation

The key is overriding `__new__` (which creates the object) to return the same instance every time:

```python
class Singleton:
    _instance = None   # class-level variable to store the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

---

## Hints

> **Hint 1:** `_instance = None` is a class variable (not instance variable). It's shared across all instances.

> **Hint 2:** `__new__` creates the object BEFORE `__init__` runs. Returning the same object prevents duplicate initialization.

> **Hint 3:** For `AppConfig`, use a dict `self._config = {}` to store settings. But only initialize it if it doesn't exist yet (to prevent resetting on repeated calls).

> **Hint 4:** In `__init__`, protect against re-initialization: `if not hasattr(self, '_initialized'): self._initialized = True; self._config = {}`.

---

## How to Run the Tests

```bash
cd level-04-expert/challenge-31-singleton-pattern
pytest tests/ -v
```
