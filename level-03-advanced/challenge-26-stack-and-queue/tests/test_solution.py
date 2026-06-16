import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import Stack, Queue


class TestStack:
    def test_new_stack_is_empty(self):
        s = Stack()
        assert s.is_empty() is True

    def test_push_makes_not_empty(self):
        s = Stack()
        s.push(1)
        assert s.is_empty() is False

    def test_push_and_pop_lifo(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        assert s.pop() == 3
        assert s.pop() == 2
        assert s.pop() == 1

    def test_pop_empty_raises(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.pop()

    def test_peek_returns_top(self):
        s = Stack()
        s.push(10)
        s.push(20)
        assert s.peek() == 20

    def test_peek_does_not_remove(self):
        s = Stack()
        s.push(10)
        s.peek()
        assert s.size() == 1

    def test_peek_empty_raises(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.peek()

    def test_size(self):
        s = Stack()
        assert s.size() == 0
        s.push(1)
        assert s.size() == 1
        s.push(2)
        assert s.size() == 2
        s.pop()
        assert s.size() == 1

    def test_push_strings(self):
        s = Stack()
        s.push("hello")
        s.push("world")
        assert s.pop() == "world"


class TestQueue:
    def test_new_queue_is_empty(self):
        q = Queue()
        assert q.is_empty() is True

    def test_enqueue_makes_not_empty(self):
        q = Queue()
        q.enqueue(1)
        assert q.is_empty() is False

    def test_enqueue_dequeue_fifo(self):
        q = Queue()
        q.enqueue("a")
        q.enqueue("b")
        q.enqueue("c")
        assert q.dequeue() == "a"
        assert q.dequeue() == "b"
        assert q.dequeue() == "c"

    def test_dequeue_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.dequeue()

    def test_front_returns_first(self):
        q = Queue()
        q.enqueue("x")
        q.enqueue("y")
        assert q.front() == "x"

    def test_front_does_not_remove(self):
        q = Queue()
        q.enqueue("x")
        q.front()
        assert q.size() == 1

    def test_front_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.front()

    def test_size(self):
        q = Queue()
        assert q.size() == 0
        q.enqueue(1)
        assert q.size() == 1
        q.enqueue(2)
        assert q.size() == 2
        q.dequeue()
        assert q.size() == 1
