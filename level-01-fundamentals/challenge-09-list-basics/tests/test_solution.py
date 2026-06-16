import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import get_first, get_last, get_length, add_item, remove_item, sort_list, sum_list


class TestGetFirst:
    def test_basic(self):
        assert get_first([10, 20, 30]) == 10

    def test_single_item(self):
        assert get_first([42]) == 42

    def test_empty_returns_none(self):
        assert get_first([]) is None

    def test_strings(self):
        assert get_first(["a", "b", "c"]) == "a"


class TestGetLast:
    def test_basic(self):
        assert get_last([10, 20, 30]) == 30

    def test_single_item(self):
        assert get_last([42]) == 42

    def test_empty_returns_none(self):
        assert get_last([]) is None

    def test_strings(self):
        assert get_last(["a", "b", "c"]) == "c"


class TestGetLength:
    def test_empty(self):
        assert get_length([]) == 0

    def test_one_item(self):
        assert get_length([99]) == 1

    def test_multiple_items(self):
        assert get_length([1, 2, 3, 4]) == 4

    def test_strings(self):
        assert get_length(["a", "b"]) == 2


class TestAddItem:
    def test_add_to_list(self):
        assert add_item([1, 2, 3], 4) == [1, 2, 3, 4]

    def test_add_to_empty(self):
        assert add_item([], "hello") == ["hello"]

    def test_add_string(self):
        assert add_item(["a", "b"], "c") == ["a", "b", "c"]

    def test_returns_list(self):
        result = add_item([1], 2)
        assert isinstance(result, list)


class TestRemoveItem:
    def test_remove_basic(self):
        assert remove_item([1, 2, 3], 2) == [1, 3]

    def test_removes_first_occurrence_only(self):
        result = remove_item([1, 2, 3, 2], 2)
        assert result == [1, 3, 2], "Only the first occurrence should be removed"

    def test_item_not_in_list(self):
        assert remove_item([1, 2, 3], 99) == [1, 2, 3]

    def test_empty_list(self):
        assert remove_item([], 1) == []

    def test_returns_list(self):
        result = remove_item([1, 2], 1)
        assert isinstance(result, list)


class TestSortList:
    def test_sort_numbers(self):
        assert sort_list([3, 1, 2]) == [1, 2, 3]

    def test_sort_already_sorted(self):
        assert sort_list([1, 2, 3]) == [1, 2, 3]

    def test_sort_empty(self):
        assert sort_list([]) == []

    def test_sort_strings(self):
        assert sort_list(["c", "a", "b"]) == ["a", "b", "c"]

    def test_does_not_modify_original(self):
        original = [3, 1, 2]
        original_copy = original.copy()
        sort_list(original)
        assert original == original_copy, "sort_list() should not modify the original list"

    def test_returns_list(self):
        result = sort_list([3, 1, 2])
        assert isinstance(result, list)


class TestSumList:
    def test_basic_sum(self):
        assert sum_list([1, 2, 3, 4]) == 10

    def test_empty_list(self):
        assert sum_list([]) == 0

    def test_single_item(self):
        assert sum_list([7]) == 7

    def test_negatives(self):
        assert sum_list([10, -5, 5]) == 10

    def test_all_zeros(self):
        assert sum_list([0, 0, 0]) == 0
