import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import double_numbers, filter_evens, squares, filter_long_words, uppercase_words


class TestDoubleNumbers:
    def test_basic(self):
        assert double_numbers([1, 2, 3, 4]) == [2, 4, 6, 8]

    def test_empty(self):
        assert double_numbers([]) == []

    def test_zero(self):
        assert double_numbers([0]) == [0]

    def test_negative(self):
        assert double_numbers([-1, -2]) == [-2, -4]

    def test_returns_list(self):
        result = double_numbers([1, 2])
        assert isinstance(result, list)


class TestFilterEvens:
    def test_mixed(self):
        assert filter_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    def test_all_odd(self):
        assert filter_evens([1, 3, 5]) == []

    def test_all_even(self):
        assert filter_evens([2, 4, 6]) == [2, 4, 6]

    def test_empty(self):
        assert filter_evens([]) == []

    def test_zero_is_even(self):
        assert 0 in filter_evens([0, 1, 2])

    def test_returns_list(self):
        result = filter_evens([1, 2, 3])
        assert isinstance(result, list)


class TestSquares:
    def test_basic(self):
        assert squares([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]

    def test_negatives(self):
        assert squares([-2, -1, 0, 1, 2]) == [4, 1, 0, 1, 4]

    def test_empty(self):
        assert squares([]) == []

    def test_single(self):
        assert squares([7]) == [49]

    def test_returns_list(self):
        result = squares([1, 2])
        assert isinstance(result, list)


class TestFilterLongWords:
    def test_basic(self):
        result = filter_long_words(["cat", "elephant", "dog", "butterfly"], 4)
        assert result == ["elephant", "butterfly"]

    def test_min_length_3(self):
        result = filter_long_words(["hi", "hello", "hey"], 3)
        assert result == ["hello", "hey"]

    def test_no_matches(self):
        result = filter_long_words(["a", "b", "c"], 5)
        assert result == []

    def test_all_match(self):
        result = filter_long_words(["hello", "world"], 3)
        assert result == ["hello", "world"]

    def test_empty(self):
        result = filter_long_words([], 3)
        assert result == []


class TestUppercaseWords:
    def test_basic(self):
        assert uppercase_words(["hello", "world"]) == ["HELLO", "WORLD"]

    def test_mixed_case(self):
        result = uppercase_words(["Mixed", "CASE"])
        assert result == ["MIXED", "CASE"]

    def test_empty(self):
        assert uppercase_words([]) == []

    def test_single_word(self):
        assert uppercase_words(["python"]) == ["PYTHON"]

    def test_returns_list(self):
        result = uppercase_words(["test"])
        assert isinstance(result, list)
