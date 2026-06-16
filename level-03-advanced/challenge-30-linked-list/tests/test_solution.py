import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import Node, LinkedList


class TestNode:
    def test_node_stores_value(self):
        n = Node(42)
        assert n.value == 42

    def test_node_next_is_none(self):
        n = Node(1)
        assert n.next is None

    def test_node_can_link(self):
        n1 = Node(1)
        n2 = Node(2)
        n1.next = n2
        assert n1.next.value == 2


class TestLinkedList:
    def test_empty_list(self):
        ll = LinkedList()
        assert ll.to_list() == []

    def test_append_single(self):
        ll = LinkedList()
        ll.append(1)
        assert ll.to_list() == [1]

    def test_append_multiple(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.to_list() == [1, 2, 3]

    def test_prepend(self):
        ll = LinkedList()
        ll.append(2)
        ll.append(3)
        ll.prepend(1)
        assert ll.to_list() == [1, 2, 3]

    def test_prepend_to_empty(self):
        ll = LinkedList()
        ll.prepend(1)
        assert ll.to_list() == [1]

    def test_delete_middle(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.delete(2)
        assert ll.to_list() == [1, 3]

    def test_delete_head(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.delete(1)
        assert ll.to_list() == [2]

    def test_delete_tail(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.delete(2)
        assert ll.to_list() == [1]

    def test_delete_not_found(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.delete(99)
        assert ll.to_list() == [1, 2]

    def test_delete_only_first_occurrence(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(2)
        ll.delete(2)
        assert ll.to_list() == [1, 2]

    def test_contains_true(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        assert ll.contains(2) is True

    def test_contains_false(self):
        ll = LinkedList()
        ll.append(1)
        assert ll.contains(99) is False

    def test_contains_empty(self):
        ll = LinkedList()
        assert ll.contains(1) is False

    def test_length(self):
        ll = LinkedList()
        assert ll.length() == 0
        ll.append(1)
        assert ll.length() == 1
        ll.append(2)
        assert ll.length() == 2

    def test_reverse(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.reverse()
        assert ll.to_list() == [3, 2, 1]

    def test_reverse_single(self):
        ll = LinkedList()
        ll.append(1)
        ll.reverse()
        assert ll.to_list() == [1]

    def test_reverse_empty(self):
        ll = LinkedList()
        ll.reverse()
        assert ll.to_list() == []
