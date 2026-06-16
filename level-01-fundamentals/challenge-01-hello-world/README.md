# Challenge 01: Hello World

**Level:** 1 – Python Fundamentals
**Difficulty:** ⭐ (Beginner)
**Estimated Time:** 15 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to use the `print()` function in Python
- How to write and call a function
- How to use f-strings to format output
- How to return values from a function

---

## Problem Description

This is your very first Python challenge. The goal is to get comfortable writing functions that produce output.

You will write three simple functions:

1. `greet(name)` — returns a greeting message for the given name
2. `describe_yourself(name, role)` — returns a sentence introducing someone
3. `format_greeting(greeting, name)` — combines a greeting word with a name

These functions might seem simple, but they teach you the fundamental building blocks of Python: functions, strings, and return values.

---

## Requirements

- [ ] `greet(name)` must return the string `"Hello, {name}!"`
- [ ] `describe_yourself(name, role)` must return `"My name is {name} and I am a {role}."`
- [ ] `format_greeting(greeting, name)` must return `"{greeting}, {name}!"`
- [ ] All functions must **return** strings, not just print them
- [ ] Use f-strings for string formatting

---

## Expected Behavior

```python
greet("Alice")
# Returns: "Hello, Alice!"

greet("Bob")
# Returns: "Hello, Bob!"

describe_yourself("Maria", "software engineer")
# Returns: "My name is Maria and I am a software engineer."

format_greeting("Good morning", "Carlos")
# Returns: "Good morning, Carlos!"

format_greeting("Hi", "World")
# Returns: "Hi, World!"
```

---

## What Is an f-string?

An f-string is a way to put variable values inside a string. You write an `f` before the opening quote, then use `{}` curly braces to insert variables:

```python
name = "Alice"
message = f"Hello, {name}!"
print(message)  # Output: Hello, Alice!
```

The `{name}` part gets replaced with the actual value of the `name` variable.

---

## What Is a Return Statement?

When a function uses `return`, it sends a value back to whoever called it. This is different from `print()`:

```python
# This just displays — no value is saved
def show(name):
    print(f"Hello, {name}!")

# This returns — the value can be saved and used
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")  # result = "Hello, Alice!"
```

In this challenge, your functions should **return** strings, not print them.

---

## Hints

> **Hint 1:** The syntax for a function is `def function_name(parameter):` followed by indented code.

> **Hint 2:** f-strings start with the letter `f` before the quote: `f"Hello, {name}!"`

> **Hint 3:** The `return` keyword sends the value back. Without `return`, your function returns `None`.

> **Hint 4:** String formatting: to put a variable inside a string, wrap it in `{}` inside an f-string.

---

## How to Run the Tests

```bash
# Navigate to this challenge folder
cd level-01-fundamentals/challenge-01-hello-world

# Run the tests
pytest tests/ -v
```

When all tests pass, you will see output like:

```
tests/test_solution.py::test_greet_basic PASSED
tests/test_solution.py::test_greet_different_names PASSED
tests/test_solution.py::test_describe_yourself PASSED
tests/test_solution.py::test_format_greeting PASSED
```

---

## Submission

When all tests pass:

```bash
git add starter.py
git commit -m "Complete challenge 01: hello world"
git push origin challenge-01-hello-world
```

Then open a Pull Request on GitHub.
