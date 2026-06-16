import argparse
import json
import os
import sys

DEFAULT_FILE = "tasks.json"


def load_tasks(filepath=DEFAULT_FILE):
    """
    TODO:
    Load tasks from a JSON file.
    Return the list of tasks.
    If the file doesn't exist, return an empty list.

    Hint:
        if not os.path.exists(filepath):
            return []
        with open(filepath, "r") as f:
            return json.load(f)
    """
    pass


def save_tasks(tasks, filepath=DEFAULT_FILE):
    """
    TODO:
    Save the list of tasks to a JSON file.

    Hint:
        with open(filepath, "w") as f:
            json.dump(tasks, f, indent=2)
    """
    pass


def add_task(title, priority="medium", filepath=DEFAULT_FILE):
    """
    TODO:
    Add a new task to the task list.
    Return the new task as a dict.

    Task format:
        {"id": <int>, "title": <str>, "priority": <str>, "done": False}

    ID should auto-increment from the highest existing ID (or 1 if empty).

    Example:
        task = add_task("Buy milk", "high")
        # Returns: {"id": 1, "title": "Buy milk", "priority": "high", "done": False}

    Hint:
        tasks = load_tasks(filepath)
        next_id = max(t["id"] for t in tasks) + 1 if tasks else 1
        task = {"id": next_id, "title": title, "priority": priority, "done": False}
        tasks.append(task)
        save_tasks(tasks, filepath)
        return task
    """
    pass


def list_tasks(priority=None, filepath=DEFAULT_FILE):
    """
    TODO:
    Return all tasks (optionally filtered by priority).
    If priority is None, return all tasks.

    Example:
        list_tasks()             → all tasks
        list_tasks("high")       → only high-priority tasks
    """
    pass


def complete_task(task_id, filepath=DEFAULT_FILE):
    """
    TODO:
    Mark the task with the given ID as done (done = True).
    Return True if found and updated, False if not found.

    Hint:
        tasks = load_tasks(filepath)
        for task in tasks:
            if task["id"] == task_id:
                task["done"] = True
                save_tasks(tasks, filepath)
                return True
        return False
    """
    pass


def delete_task(task_id, filepath=DEFAULT_FILE):
    """
    TODO:
    Delete the task with the given ID.
    Return True if deleted, False if not found.

    Hint:
        tasks = load_tasks(filepath)
        original_len = len(tasks)
        tasks = [t for t in tasks if t["id"] != task_id]
        if len(tasks) == original_len:
            return False
        save_tasks(tasks, filepath)
        return True
    """
    pass


def build_parser():
    """
    TODO:
    Build and return an argparse.ArgumentParser with subcommands:

    Subcommand: add
        Positional: title (str)
        Optional: --priority (choices: high, medium, low; default: medium)

    Subcommand: list
        Optional: --priority (choices: high, medium, low)

    Subcommand: complete
        Positional: id (int)

    Subcommand: delete
        Positional: id (int)
    """
    parser = argparse.ArgumentParser(
        prog="tasks",
        description="Simple task manager CLI"
    )
    subparsers = parser.add_subparsers(dest="command")

    # TODO: add subcommand
    # add_parser = subparsers.add_parser("add", help="Add a new task")
    # add_parser.add_argument("title", help="Task title")
    # add_parser.add_argument("--priority", choices=["high", "medium", "low"], default="medium")

    # TODO: list subcommand
    # list_parser = subparsers.add_parser("list", help="List tasks")
    # list_parser.add_argument("--priority", choices=["high", "medium", "low"])

    # TODO: complete subcommand
    # complete_parser = subparsers.add_parser("complete", help="Mark task as complete")
    # complete_parser.add_argument("id", type=int)

    # TODO: delete subcommand
    # delete_parser = subparsers.add_parser("delete", help="Delete a task")
    # delete_parser.add_argument("id", type=int)

    return parser


def main():
    """
    TODO:
    Parse arguments and call the appropriate function.

    If no command is given, print help and exit.

    Example behavior:
        args.command == "add"      → call add_task(args.title, args.priority)
        args.command == "list"     → call list_tasks(args.priority)
        args.command == "complete" → call complete_task(args.id)
        args.command == "delete"   → call delete_task(args.id)

    Print output:
        add:      f"Added task #{task['id']}: '{task['title']}' [{task['priority']}]"
        list:     f"#{t['id']} [{'x' if t['done'] else ' '}] {t['title']} [{t['priority']}]" for each task
        complete: f"Task #{id} marked as complete."  or  "Task #{id} not found."
        delete:   f"Task #{id} deleted."  or  "Task #{id} not found."
    """
    parser = build_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    # TODO: Handle each command


if __name__ == "__main__":
    main()
