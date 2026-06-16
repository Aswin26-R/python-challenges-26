import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import merge, merge_sort, merge_sort_inplace


class TestMerge:
    def test_basic_merge(self):
        assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    def test_empty_right(self):
        assert merge([1, 2, 3], []) == [1, 2, 3]

    def test_empty_left(self):
        assert merge([], [4, 5]) == [4, 5]

    def test_both_single(self):
        assert merge([1], [2]) == [1, 2]

    def test_both_single_reversed(self):
        assert merge([2], [1]) == [1, 2]

    def test_both_empty(self):
        assert merge([], []) == []

    def test_returns_sorted(self):
        result = merge([1, 4, 7], [2, 5, 8])
        assert result == sorted(result)


class TestMergeSort:
    def test_basic_sort(self):
        assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]

    def test_empty(self):
        assert merge_sort([]) == []

    def test_single(self):
        assert merge_sort([1]) == [1]

    def test_two_elements(self):
        assert merge_sort([2, 1]) == [1, 2]

    def test_already_sorted(self):
        assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_does_not_modify_original(self):
        original = [3, 1, 2]
        merge_sort(original)
        assert original == [3, 1, 2], "merge_sort should return a NEW list, not modify the original"

    def test_returns_list(self):
        result = merge_sort([3, 1, 2])
        assert isinstance(result, list)

    def test_large_list(self):
        import random
        data = list(range(100))
        random.shuffle(data)
        assert merge_sort(data) == list(range(100))


class TestMergeSortInplace:
    def test_basic_inplace(self):
        data = [3, 1, 4, 1, 5]
        merge_sort_inplace(data)
        assert data == [1, 1, 3, 4, 5]

    def test_modifies_original(self):
        data = [3, 1, 2]
        original_id = id(data)
        merge_sort_inplace(data)
        assert id(data) == original_id, "merge_sort_inplace should modify the original list"

    def test_empty(self):
        data = []
        merge_sort_inplace(data)
        assert data == []

    def test_single(self):
        data = [1]
        merge_sort_inplace(data)
        assert data == [1]
