# Challenge 38: CLI Tool

**Level:** 4 – Expert Python
**Difficulty:** ⭐⭐⭐⭐ (Expert)
**Estimated Time:** 80 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to build command-line tools with `argparse`
- How to define subcommands (like `git commit`, `git push`)
- How to validate command-line arguments
- How to handle arguments with types, defaults, and help text
- Professional CLI design patterns

---

## Problem Description

Real Python tools (like `pip`, `git`, `pytest`) are command-line tools. In this challenge, you'll build a simple **task manager CLI** that supports multiple subcommands.

---

## Requirements

Build a CLI tool for managing tasks with these subcommands:

- `add <title> [--priority high|medium|low]` — add a task
- `list [--priority <level>]` — list all tasks (optionally filtered by priority)
- `complete <id>` — mark task as complete
- `delete <id>` — delete a task

The tool stores tasks in a JSON file.

---

## Expected Usage

```bash
python starter.py add "Buy milk" --priority high
# Output: Added task #1: 'Buy milk' [high]

python starter.py add "Write report"
# Output: Added task #2: 'Write report' [medium]

python starter.py list
# Output:
# #1 [ ] Buy milk [high]
# #2 [ ] Write report [medium]

python starter.py list --priority high
# Output:
# #1 [ ] Buy milk [high]

python starter.py complete 1
# Output: Task #1 marked as complete.

python starter.py list
# Output:
# #1 [x] Buy milk [high]
# #2 [ ] Write report [medium]

python starter.py delete 2
# Output: Task #2 deleted.
```

---

## argparse Basics

```python
import argparse

parser = argparse.ArgumentParser(description="My CLI tool")
subparsers = parser.add_subparsers(dest="command")

# Subcommand: add
add_parser = subparsers.add_parser("add", help="Add a task")
add_parser.add_argument("title", help="Task title")
add_parser.add_argument("--priority", choices=["high", "medium", "low"],
                         default="medium", help="Task priority")

# Parse arguments:
args = parser.parse_args()
if args.command == "add":
    add_task(args.title, args.priority)
```

---

## JSON Storage Format

```json
[
  {"id": 1, "title": "Buy milk", "priority": "high", "done": false},
  {"id": 2, "title": "Write report", "priority": "medium", "done": false}
]
```

---

## Hints

> **Hint 1:** Store tasks in a JSON file. `json.load(f)` reads, `json.dump(tasks, f, indent=2)` writes.

> **Hint 2:** Auto-increment IDs: `next_id = max(t["id"] for t in tasks) + 1` or `1` if empty.

> **Hint 3:** The `complete` and `delete` subcommands take `id` as an integer: `parser.add_argument("id", type=int)`.

> **Hint 4:** Separate business logic from CLI parsing — write `add_task()`, `list_tasks()`, etc. as plain functions the tests can call directly.

---

## How to Run the Tests

```bash
cd level-04-expert/challenge-38-cli-tool
pytest tests/ -v

# Also try it manually:
python starter.py add "Write tests" --priority high
python starter.py list
python starter.py complete 1
```
