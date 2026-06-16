# Python Challenges – Internship Program

Welcome! This repository contains **40 Python programming challenges** designed for our internship program.

If you have never written Python before — that is perfectly fine.
If you have never used Git or GitHub before — also perfectly fine.
This guide explains everything from scratch.

Read this entire document before starting your first challenge.

---

## Table of Contents

1. [What Is This Repository?](#1-what-is-this-repository)
2. [Why Are You Doing These Challenges?](#2-why-are-you-doing-these-challenges)
3. [How the Internship Workflow Works](#3-how-the-internship-workflow-works)
4. [Before You Start – Setting Up](#4-before-you-start--setting-up)
5. [Step 1 – Fork the Repository](#5-step-1--fork-the-repository)
6. [Step 2 – Clone Your Fork](#6-step-2--clone-your-fork)
7. [Step 3 – Create a Branch](#7-step-3--create-a-branch)
8. [Step 4 – Write Your Solution](#8-step-4--write-your-solution)
9. [Step 5 – Commit Your Changes](#9-step-5--commit-your-changes)
10. [Step 6 – Push Your Code](#10-step-6--push-your-code)
11. [Step 7 – Open a Pull Request](#11-step-7--open-a-pull-request)
12. [How Mentors Review Your Work](#12-how-mentors-review-your-work)
13. [How to Respond to Review Comments](#13-how-to-respond-to-review-comments)
14. [How to Update a Pull Request](#14-how-to-update-a-pull-request)
15. [Challenge Index](#15-challenge-index)
16. [Frequently Asked Questions](#16-frequently-asked-questions)

---

## 1. What Is This Repository?

This repository is your Python learning hub for the internship. It contains 40 carefully designed programming challenges that take you from absolute beginner to advanced Python developer.

**The challenges are organized into four levels:**

| Level | Name | Challenges | Who It's For |
|-------|------|------------|--------------|
| Level 1 | Python Fundamentals | 01 – 10 | Complete beginners |
| Level 2 | Intermediate Python | 11 – 20 | Comfortable with basics |
| Level 3 | Advanced Python | 21 – 30 | Ready for real-world patterns |
| Level 4 | Expert Python | 31 – 40 | Building production-quality code |

Complete challenges in order. Each one builds on the previous.

---

## 2. Why Are You Doing These Challenges?

These challenges exist for three reasons:

**Reason 1 – Learn Python properly.**
Reading tutorials is not the same as writing code. These challenges force you to think, make mistakes, fix them, and understand why things work.

**Reason 2 – Learn professional Git workflow.**
Every software company uses Git. Every pull request you open here is practice for the real work you will do on the job. By the end, opening a PR will feel natural.

**Reason 3 – Build a reviewable portfolio.**
Your pull requests are your work history. Mentors can see how you think, how you write code, and how you respond to feedback. This is how you grow.

---

## 3. How the Internship Workflow Works

Here is the big picture:

```
zad-internship/python-challenges (this repo)
         |
         | You "fork" it → creates your own copy on GitHub
         ↓
Your Fork on GitHub
         |
         | You "clone" it → downloads it to your computer
         ↓
Your Computer (local copy)
         |
         | You create a branch, write code, commit
         ↓
         | You "push" → sends your code back to YOUR fork on GitHub
         ↓
Your Fork on GitHub (updated)
         |
         | You open a "Pull Request" → asks company repo to review your work
         ↓
zad-internship/python-challenges receives Pull Request
         |
         | Mentor reviews your code and leaves comments
         ↓
         | You update your code based on feedback
         ↓
         | PR stays open as your submission record (NOT merged)
```

> **Important:** Pull Requests in this program are your submissions. They are **not merged** into the main repository. They stay open so mentors can review and track your progress.

---

## 4. Before You Start – Setting Up

You need three things on your computer before you can begin.

### Install Python

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.11 or newer
3. On Windows: during installation, check **"Add Python to PATH"**
4. Verify it worked:

```bash
python --version
# Expected output: Python 3.11.x
```

### Install Git

1. Go to [git-scm.com](https://git-scm.com/) and install Git
2. Verify it worked:

```bash
git --version
# Expected output: git version 2.x.x
```

### Install pytest

```bash
pip install pytest
pytest --version
```

### Create a GitHub Account

Go to [github.com](https://github.com) and sign up. Use a professional username — you will use it for years.

### Configure Git with Your Identity

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
```

This information appears on every commit you make.

---

## 5. Step 1 – Fork the Repository

**What is a fork?**
A fork is your own personal copy of this repository on your GitHub account. You cannot push directly to `zad-internship/python-challenges` — you push to your fork instead.

**How to fork:**

1. Log into GitHub
2. Go to `https://github.com/zad-internship/python-challenges`
3. Click the **"Fork"** button in the top-right corner
4. Choose your personal account as the destination
5. Wait a few seconds while GitHub copies the repository

After forking, you will have:
`https://github.com/YOUR-USERNAME/python-challenges`

This is YOUR copy. You own it and can push to it freely.

---

## 6. Step 2 – Clone Your Fork

**What is cloning?**
Cloning downloads the repository from GitHub to your computer so you can work on it locally.

**How to clone:**

1. Go to YOUR fork on GitHub (not `zad-internship/python-challenges`)
2. Click the green **"Code"** button
3. Make sure **HTTPS** is selected
4. Copy the URL: `https://github.com/YOUR-USERNAME/python-challenges.git`
5. Open your terminal and navigate to where you want the project:

```bash
cd Documents
```

6. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/python-challenges.git
```

7. Move into the folder:

```bash
cd python-challenges
```

**Verify it worked:**

```bash
git status
# Output: On branch main, nothing to commit, working tree clean
```

---

## 7. Step 3 – Create a Branch

**What is a branch?**
A branch is an isolated workspace for your code. Changes on one branch do not affect other branches. Think of it like a separate notebook for each challenge.

**Why one branch per challenge?**
Each challenge is separate work. One branch = one challenge = one clean Pull Request.

**How to create a branch:**

```bash
git checkout -b challenge-01-hello-world
```

What this does:
- `-b` creates a new branch
- `checkout` switches you to that branch
- One command does both: create AND switch

**Branch naming convention:**

```
challenge-01-hello-world
challenge-07-fizzbuzz
challenge-15-dictionary-operations
```

Always: lowercase, hyphens between words, include the challenge number.

**Verify you are on the right branch:**

```bash
git branch
# The branch with * is your current branch
```

> **Rule:** Always create new branches from `main`. Never create a branch from another challenge branch.

---

## 8. Step 4 – Write Your Solution

Each challenge has this structure:

```
level-01-fundamentals/
└── challenge-01-hello-world/
    ├── README.md          ← Read this first
    ├── starter.py         ← Write your solution here
    └── tests/
        └── test_solution.py  ← Automated tests
```

**Your workflow:**

1. Read `README.md` — understand the problem fully
2. Open `starter.py` — read the TODO comments
3. Write your solution
4. Run the tests

**Running tests:**

```bash
# From inside the challenge folder:
pytest tests/ -v

# From the repository root:
pytest level-01-fundamentals/challenge-01-hello-world/tests/ -v
```

Green output = passing tests. Red output = failing tests with details on what went wrong.

---

## 9. Step 5 – Commit Your Changes

**What is a commit?**
A commit is a saved snapshot of your code. Git records what changed, when, and who did it.

**Step 1 – Stage your file:**

```bash
git add starter.py
```

This tells Git: "Include this file in my next commit."

**Step 2 – Create the commit:**

```bash
git commit -m "Complete challenge 01: hello world"
```

**Good commit messages:**
- `git commit -m "Complete challenge 01: hello world"`
- `git commit -m "Fix failing test in challenge 03"`
- `git commit -m "Improve challenge 07: handle zero edge case"`

**Bad commit messages:**
- `git commit -m "done"` — too vague
- `git commit -m "stuff"` — meaningless
- `git commit -m "aaa"` — unprofessional

**Verify your commit:**

```bash
git log --oneline
```

---

## 10. Step 6 – Push Your Code

**What is pushing?**
Pushing sends your local commits up to GitHub. Until you push, your work only exists on your machine.

**How to push:**

```bash
git push origin challenge-01-hello-world
```

- `origin` — the name for your GitHub fork (set up automatically when you cloned)
- `challenge-01-hello-world` — the branch you are pushing

**First time pushing a branch:**

```bash
git push --set-upstream origin challenge-01-hello-world
```

After this, future pushes on this branch just need `git push`.

**Verify it worked:**
Go to your fork on GitHub. You will see:
> "challenge-01-hello-world had recent pushes — Compare & pull request"

---

## 11. Step 7 – Open a Pull Request

**What is a Pull Request (PR)?**
A Pull Request is a formal code submission. It shows mentors exactly what you wrote and gives them a place to leave feedback.

**How to open a PR:**

1. Go to YOUR fork on GitHub
2. Click **"Compare & pull request"** (yellow banner)
3. Verify the settings:
   - **Base repository:** `zad-internship/python-challenges`
   - **Base branch:** `main`
   - **Head repository:** YOUR fork
   - **Compare branch:** `challenge-01-hello-world`
4. Title format: `[Challenge 01] Hello World – Your Name`
5. Fill in the PR description template
6. Click **"Create pull request"**

> **Do NOT click "Merge pull request".** These PRs are submissions, not merges.

---

## 12. How Mentors Review Your Work

Mentors may:

- **Leave inline comments** on specific lines of your code
- **Request changes** if the solution needs improvement (you get an email)
- **Approve** if the solution is good

**What mentors check:**
- Do all tests pass?
- Is the code readable and clean?
- Are variable names descriptive?
- Are edge cases handled?
- Did you understand the problem?

---

## 13. How to Respond to Review Comments

1. Open your PR on GitHub
2. Read each comment carefully
3. Reply to the comment if you have a question
4. Fix your code (see next section)
5. After pushing, reply to the comment explaining what you changed:

> "Fixed — changed `range(len(items))` to `enumerate(items)` as suggested."

---

## 14. How to Update a Pull Request

After mentor feedback, update the SAME PR. Do not open a new one.

```bash
# Switch back to your branch
git checkout challenge-01-hello-world

# Edit starter.py to fix the issue

# Stage and commit
git add starter.py
git commit -m "Fix: address review feedback on variable naming"

# Push — the PR updates automatically
git push
```

The full cycle:

```
Mentor leaves comment
        ↓
git checkout challenge-01-hello-world
        ↓
Edit starter.py
        ↓
git add starter.py
git commit -m "Fix: address feedback"
git push
        ↓
PR on GitHub updates automatically
        ↓
Reply to mentor comment explaining your change
```

---

## 15. Challenge Index

### Level 1 – Python Fundamentals

| # | Challenge | Topic | Est. Time |
|---|-----------|-------|-----------|
| 01 | [Hello World](level-01-fundamentals/challenge-01-hello-world/) | print, f-strings | 15 min |
| 02 | [Variables and Types](level-01-fundamentals/challenge-02-variables-and-types/) | int, float, str, bool | 20 min |
| 03 | [Even or Odd](level-01-fundamentals/challenge-03-even-or-odd/) | if/else, modulo | 20 min |
| 04 | [Basic Calculator](level-01-fundamentals/challenge-04-basic-calculator/) | functions, arithmetic | 25 min |
| 05 | [String Reversal](level-01-fundamentals/challenge-05-string-reversal/) | strings, slicing | 20 min |
| 06 | [Palindrome Checker](level-01-fundamentals/challenge-06-palindrome-checker/) | string comparison | 25 min |
| 07 | [FizzBuzz](level-01-fundamentals/challenge-07-fizzbuzz/) | loops, conditions | 25 min |
| 08 | [Temperature Converter](level-01-fundamentals/challenge-08-temperature-converter/) | math, functions | 25 min |
| 09 | [List Basics](level-01-fundamentals/challenge-09-list-basics/) | lists, methods | 30 min |
| 10 | [Grade Calculator](level-01-fundamentals/challenge-10-grade-calculator/) | dicts, averaging | 35 min |

### Level 2 – Intermediate Python

| # | Challenge | Topic | Est. Time |
|---|-----------|-------|-----------|
| 11 | [Word Frequency](level-02-intermediate/challenge-11-word-frequency/) | dicts, strings | 35 min |
| 12 | [Fibonacci Sequence](level-02-intermediate/challenge-12-fibonacci-sequence/) | loops, sequences | 30 min |
| 13 | [Prime Checker](level-02-intermediate/challenge-13-prime-checker/) | math, loops | 35 min |
| 14 | [List Comprehensions](level-02-intermediate/challenge-14-list-comprehensions/) | comprehensions | 35 min |
| 15 | [Dictionary Operations](level-02-intermediate/challenge-15-dictionary-operations/) | dict CRUD | 40 min |
| 16 | [Exception Handling](level-02-intermediate/challenge-16-exception-handling/) | try/except | 40 min |
| 17 | [Classes and Objects](level-02-intermediate/challenge-17-classes-and-objects/) | OOP basics | 45 min |
| 18 | [Recursion Factorial](level-02-intermediate/challenge-18-recursion-factorial/) | recursion | 40 min |
| 19 | [String Manipulation](level-02-intermediate/challenge-19-string-manipulation/) | string methods | 40 min |
| 20 | [Number Guessing Game](level-02-intermediate/challenge-20-number-guessing-game/) | random, while | 45 min |

### Level 3 – Advanced Python

| # | Challenge | Topic | Est. Time |
|---|-----------|-------|-----------|
| 21 | [Decorators](level-03-advanced/challenge-21-decorators/) | @wrapper, closures | 60 min |
| 22 | [Generators](level-03-advanced/challenge-22-generators/) | yield, lazy eval | 60 min |
| 23 | [Context Managers](level-03-advanced/challenge-23-context-managers/) | with, __enter__ | 60 min |
| 24 | [Functional Programming](level-03-advanced/challenge-24-functional-programming/) | map, filter, reduce | 55 min |
| 25 | [Regular Expressions](level-03-advanced/challenge-25-regular-expressions/) | re module | 60 min |
| 26 | [Stack and Queue](level-03-advanced/challenge-26-stack-and-queue/) | custom data structs | 60 min |
| 27 | [Binary Search](level-03-advanced/challenge-27-binary-search/) | divide and conquer | 55 min |
| 28 | [Inheritance and Polymorphism](level-03-advanced/challenge-28-inheritance-polymorphism/) | OOP hierarchy | 70 min |
| 29 | [File Processing](level-03-advanced/challenge-29-file-processing/) | file I/O, CSV | 65 min |
| 30 | [Linked List](level-03-advanced/challenge-30-linked-list/) | nodes, pointers | 70 min |

### Level 4 – Expert Python

| # | Challenge | Topic | Est. Time |
|---|-----------|-------|-----------|
| 31 | [Singleton Pattern](level-04-expert/challenge-31-singleton-pattern/) | design patterns | 75 min |
| 32 | [Merge Sort](level-04-expert/challenge-32-merge-sort/) | recursive sorting | 70 min |
| 33 | [Graph Traversal](level-04-expert/challenge-33-graph-traversal/) | BFS, DFS | 90 min |
| 34 | [Async Programming](level-04-expert/challenge-34-async-programming/) | asyncio | 90 min |
| 35 | [API Client](level-04-expert/challenge-35-api-client/) | HTTP, requests | 80 min |
| 36 | [SQLite Database](level-04-expert/challenge-36-sqlite-database/) | sqlite3, SQL | 90 min |
| 37 | [Memoization and Caching](level-04-expert/challenge-37-memoization-caching/) | lru_cache, perf | 75 min |
| 38 | [CLI Tool](level-04-expert/challenge-38-cli-tool/) | argparse, CLI UX | 80 min |
| 39 | [Data Pipeline](level-04-expert/challenge-39-data-pipeline/) | ETL, chaining | 90 min |
| 40 | [Mini Bank System](level-04-expert/challenge-40-mini-bank-system/) | full OOP project | 120 min |

---

## 16. Frequently Asked Questions

### What if my tests fail?

Failing tests are normal — they are designed to fail until your code is correct. Read the error message:

```
FAILED tests/test_solution.py::test_is_even - AssertionError: assert False == True
```

This tells you: the test called `is_even()`, expected `True`, but got `False`. Fix your code accordingly.

---

### What if I accidentally break something?

Undo changes to a file since your last commit:

```bash
git checkout -- starter.py
```

> Warning: This permanently discards unsaved changes. Run `git diff` first to preview.

---

### What if I don't understand the problem?

In order:
1. Re-read the challenge README slowly
2. Study the example input/output
3. Read the hints section
4. Look at the test file — tests show exactly what your function should return
5. Ask your mentor via PR comment or Slack

---

### Can I use AI tools like ChatGPT?

**Allowed:**
- Using AI to understand a concept ("What is a Python dictionary?")
- Using AI to explain an error message
- Using AI to learn about a built-in function

**Not allowed:**
- Asking AI to write your solution
- Copying AI code without understanding it

Mentors can tell the difference. If you didn't write it, you won't be able to explain it during review.

---

### How do I ask for help?

Always share: the exact error message, the code you wrote, what you expected, what actually happened.

Channels in order: read the error → check hints → Google → ask on Slack → comment on your PR.

---

### How do I start the next challenge?

Always start from `main`:

```bash
git checkout main
git checkout -b challenge-02-variables-and-types
```

Never create a branch from another challenge branch.

---

### How do I know if I passed?

```bash
pytest tests/ -v
```

When all tests show `PASSED`, you are ready to submit.

---

### Quick Command Reference

```bash
# One-time setup
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
git clone https://github.com/YOUR-USERNAME/python-challenges.git
cd python-challenges

# Start each challenge
git checkout main
git checkout -b challenge-XX-name

# Submit a challenge
git add starter.py
git commit -m "Complete challenge XX: description"
git push origin challenge-XX-name
# Then open a PR on GitHub

# Update after mentor feedback
git checkout challenge-XX-name
# ... fix your code ...
git add starter.py
git commit -m "Fix: address review feedback"
git push

# Run tests
pytest tests/ -v

# Useful status commands
git status        # what changed?
git branch        # which branch am I on?
git log --oneline # recent commits
```

---

Your mentors are here to help. Ask questions early, ask questions often.

Every professional developer started exactly where you are now.
