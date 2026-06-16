# Challenge 34: Async Programming

**Level:** 4 – Expert Python
**Difficulty:** ⭐⭐⭐⭐ (Expert)
**Estimated Time:** 90 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- What asynchronous programming is and why it exists
- The `async def` and `await` keywords
- How `asyncio.gather()` runs tasks concurrently
- The difference between async and multi-threading
- When to use async (I/O-bound) vs threads (CPU-bound)

---

## Problem Description

Asynchronous programming allows Python to do other work while waiting for slow operations (network requests, file I/O, database queries). Instead of blocking and wasting time, the program can start another task.

---

## Requirements

- [ ] `async_greet(name, delay)` — async function that waits `delay` seconds then returns a greeting
- [ ] `fetch_multiple(names, delay)` — fetches all greetings concurrently using `asyncio.gather()`
- [ ] `async_countdown(start)` — async generator that counts down with a small delay
- [ ] `run_with_timeout(coro, timeout)` — runs a coroutine with a timeout, returns `None` if it times out

---

## Expected Behavior

```python
import asyncio

# Run single coroutine:
result = asyncio.run(async_greet("Alice", 0.01))
# Returns: "Hello, Alice!"

# Run multiple concurrently (much faster than sequential):
results = asyncio.run(fetch_multiple(["Alice", "Bob", "Charlie"], 0.01))
# Returns: ["Hello, Alice!", "Hello, Bob!", "Hello, Charlie!"]

# With timeout:
result = asyncio.run(run_with_timeout(async_greet("Alice", 5), timeout=0.01))
# Returns: None  (timed out)
```

---

## Why Async?

```python
# Sequential (slow — each waits for the previous):
for name in names:
    result = await fetch(name)   # 1 second each = 3 seconds total

# Concurrent with gather (fast — all run at the same time):
results = await asyncio.gather(*[fetch(name) for name in names])
# 3 fetches at once = ~1 second total
```

---

## Key Concepts

```python
async def my_function():    # define a coroutine
    await asyncio.sleep(1)  # yield control while sleeping
    return "done"

# Run it:
asyncio.run(my_function())

# Run multiple concurrently:
asyncio.gather(coro1(), coro2(), coro3())
```

---

## Hints

> **Hint 1:** `async_greet`: `async def async_greet(name, delay): await asyncio.sleep(delay); return f"Hello, {name}!"`

> **Hint 2:** `fetch_multiple`: `return list(await asyncio.gather(*[async_greet(n, delay) for n in names]))`

> **Hint 3:** `run_with_timeout`: use `asyncio.wait_for(coro, timeout=timeout)` wrapped in try/except `asyncio.TimeoutError`.

> **Hint 4:** `async_countdown`: use `async def` with `yield` — this creates an async generator.

---

## How to Run the Tests

```bash
cd level-04-expert/challenge-34-async-programming
pytest tests/ -v
```
