import pytest
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import load_tasks, save_tasks, add_task, list_tasks, complete_task, delete_task, build_parser


@pytest.fixture
def task_file(tmp_path):
    return str(tmp_path / "tasks.json")


class TestLoadSave:
    def test_load_empty_when_no_file(self, task_file):
        assert load_tasks(task_file) == []

    def test_save_and_load(self, task_file):
        tasks = [{"id": 1, "title": "Test", "priority": "low", "done": False}]
        save_tasks(tasks, task_file)
        assert load_tasks(task_file) == tasks


class TestAddTask:
    def test_add_task_returns_dict(self, task_file):
        task = add_task("Buy milk", "high", task_file)
        assert isinstance(task, dict)

    def test_add_task_fields(self, task_file):
        task = add_task("Buy milk", "high", task_file)
        assert task["title"] == "Buy milk"
        assert task["priority"] == "high"
        assert task["done"] is False
        assert "id" in task

    def test_add_task_auto_id(self, task_file):
        t1 = add_task("First", "low", task_file)
        t2 = add_task("Second", "medium", task_file)
        assert t2["id"] == t1["id"] + 1

    def test_add_task_default_priority(self, task_file):
        task = add_task("Test task", filepath=task_file)
        assert task["priority"] == "medium"

    def test_add_persists_to_file(self, task_file):
        add_task("Test", "high", task_file)
        loaded = load_tasks(task_file)
        assert len(loaded) == 1


class TestListTasks:
    def test_list_all(self, task_file):
        add_task("A", "high", task_file)
        add_task("B", "low", task_file)
        tasks = list_tasks(filepath=task_file)
        assert len(tasks) == 2

    def test_list_filter_by_priority(self, task_file):
        add_task("A", "high", task_file)
        add_task("B", "low", task_file)
        add_task("C", "high", task_file)
        high_tasks = list_tasks(priority="high", filepath=task_file)
        assert len(high_tasks) == 2
        assert all(t["priority"] == "high" for t in high_tasks)

    def test_list_empty(self, task_file):
        assert list_tasks(filepath=task_file) == []


class TestCompleteTask:
    def test_complete_sets_done(self, task_file):
        task = add_task("Test", "low", task_file)
        complete_task(task["id"], task_file)
        tasks = load_tasks(task_file)
        assert tasks[0]["done"] is True

    def test_complete_returns_true(self, task_file):
        task = add_task("Test", "low", task_file)
        assert complete_task(task["id"], task_file) is True

    def test_complete_missing_returns_false(self, task_file):
        assert complete_task(999, task_file) is False


class TestDeleteTask:
    def test_delete_removes_task(self, task_file):
        task = add_task("Test", "low", task_file)
        delete_task(task["id"], task_file)
        assert load_tasks(task_file) == []

    def test_delete_returns_true(self, task_file):
        task = add_task("Test", "low", task_file)
        assert delete_task(task["id"], task_file) is True

    def test_delete_missing_returns_false(self, task_file):
        assert delete_task(999, task_file) is False


class TestBuildParser:
    def test_parser_has_add_command(self):
        parser = build_parser()
        args = parser.parse_args(["add", "My task"])
        assert args.command == "add"
        assert args.title == "My task"

    def test_add_default_priority(self):
        parser = build_parser()
        args = parser.parse_args(["add", "Task"])
        assert args.priority == "medium"

    def test_add_custom_priority(self):
        parser = build_parser()
        args = parser.parse_args(["add", "Task", "--priority", "high"])
        assert args.priority == "high"

    def test_list_command(self):
        parser = build_parser()
        args = parser.parse_args(["list"])
        assert args.command == "list"

    def test_complete_command(self):
        parser = build_parser()
        args = parser.parse_args(["complete", "3"])
        assert args.command == "complete"
        assert args.id == 3

    def test_delete_command(self):
        parser = build_parser()
        args = parser.parse_args(["delete", "5"])
        assert args.command == "delete"
        assert args.id == 5
