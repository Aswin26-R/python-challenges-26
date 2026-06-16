import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import binary_search_iterative, binary_search_recursive, find_insert_position


class TestBinarySearchIterative:
    def test_found_middle(self):
        assert binary_search_iterative([1, 3, 5, 7, 9, 11], 7) == 3

    def test_not_found(self):
        assert binary_search_iterative([1, 3, 5, 7, 9, 11], 4) == -1

    def test_found_first(self):
        assert binary_search_iterative([1, 3, 5, 7, 9, 11], 1) == 0

    def test_found_last(self):
        assert binary_search_iterative([1, 3, 5, 7, 9, 11], 11) == 5

    def test_empty_list(self):
        assert binary_search_iterative([], 5) == -1

    def test_single_element_found(self):
        assert binary_search_iterative([42], 42) == 0

    def test_single_element_not_found(self):
        assert binary_search_iterative([42], 7) == -1

    def test_returns_correct_index(self):
        arr = [2, 4, 6, 8, 10, 12, 14]
        idx = binary_search_iterative(arr, 8)
        assert arr[idx] == 8


class TestBinarySearchRecursive:
    def test_found_middle(self):
        assert binary_search_recursive([1, 3, 5, 7, 9, 11], 7) == 3

    def test_not_found(self):
        assert binary_search_recursive([1, 3, 5, 7, 9, 11], 4) == -1

    def test_found_first(self):
        assert binary_search_recursive([1, 3, 5, 7, 9, 11], 1) == 0

    def test_found_last(self):
        assert binary_search_recursive([1, 3, 5, 7, 9, 11], 11) == 5

    def test_empty_list(self):
        assert binary_search_recursive([], 5) == -1

    def test_matches_iterative(self):
        arr = list(range(0, 100, 2))
        for target in [0, 10, 50, 99, 100]:
            assert binary_search_recursive(arr, target) == binary_search_iterative(arr, target)


class TestFindInsertPosition:
    def test_middle(self):
        assert find_insert_position([1, 3, 5, 7, 9], 4) == 2

    def test_before_all(self):
        assert find_insert_position([1, 3, 5, 7, 9], 0) == 0

    def test_after_all(self):
        assert find_insert_position([1, 3, 5, 7, 9], 10) == 5

    def test_exact_match(self):
        assert find_insert_position([1, 3, 5, 7, 9], 5) == 2

    def test_empty_list(self):
        assert find_insert_position([], 5) == 0

    def test_insert_keeps_order(self):
        arr = [1, 3, 5, 7, 9]
        pos = find_insert_position(arr, 4)
        arr.insert(pos, 4)
        assert arr == [1, 3, 4, 5, 7, 9]
