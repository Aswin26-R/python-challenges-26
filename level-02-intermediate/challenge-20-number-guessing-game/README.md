# Challenge 20: Number Guessing Game Logic

**Level:** 2 – Intermediate Python
**Difficulty:** ⭐⭐ (Intermediate)
**Estimated Time:** 45 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to use the `random` module
- How to write game logic with state
- How to return structured results from functions
- How to think about game flow as a series of functions

---

## Problem Description

You will implement the core logic of a number guessing game. The player tries to guess a secret number. After each guess, they get feedback: "too high", "too low", or "correct".

Instead of building a full interactive game (which can't be easily tested), you will write the logic as pure functions that can be tested and then composed into a game.

---

## Requirements

- [ ] `generate_secret_number(min_val, max_val)` — returns a random integer in the range (inclusive)
- [ ] `check_guess(secret, guess)` — returns `"too_low"`, `"too_high"`, or `"correct"`
- [ ] `play_round(secret, guess, attempts)` — returns a dict with result info
- [ ] `calculate_score(attempts, max_attempts)` — returns a score from 0–100

---

## Expected Behavior

```python
generate_secret_number(1, 10)
# Returns: a random int between 1 and 10 (e.g., 7)

check_guess(7, 5)
# Returns: "too_low"

check_guess(7, 9)
# Returns: "too_high"

check_guess(7, 7)
# Returns: "correct"

play_round(7, 5, 3)
# Returns: {
#     "guess": 5,
#     "result": "too_low",
#     "attempts": 3,
#     "game_over": False
# }

play_round(7, 7, 2)
# Returns: {
#     "guess": 7,
#     "result": "correct",
#     "attempts": 2,
#     "game_over": True
# }

calculate_score(1, 10)
# Returns: 100  (got it on first try out of 10)

calculate_score(10, 10)
# Returns: 0  (used all attempts)

calculate_score(5, 10)
# Returns: 50
```

---

## Hints

> **Hint 1:** `import random` at the top, then `random.randint(min_val, max_val)` for inclusive random int.

> **Hint 2:** `check_guess()` — three conditions: guess < secret, guess > secret, or equal.

> **Hint 3:** `play_round()` uses `check_guess()` to get the result, then builds and returns a dict. `game_over` is `True` when `result == "correct"`.

> **Hint 4:** `calculate_score()` formula: `max(0, int(100 * (max_attempts - attempts) / (max_attempts - 1)))` — but you can use any reasonable formula that gives 100 for 1 attempt and 0 for max attempts.

---

## How to Run the Tests

```bash
cd level-02-intermediate/challenge-20-number-guessing-game
pytest tests/ -v
```
