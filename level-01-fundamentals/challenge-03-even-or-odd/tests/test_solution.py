import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import is_even, is_odd, classify_number


class TestIsEven:
    def test_even_number(self):
        assert is_even(4) is True

    def test_odd_number(self):
        assert is_even(7) is False

    def test_zero_is_even(self):
        assert is_even(0) is True, "Zero is an even number (0 % 2 == 0)"

    def test_large_even(self):
        assert is_even(100) is True

    def test_large_odd(self):
        assert is_even(99) is False

    def test_negative_even(self):
        assert is_even(-4) is True

    def test_negative_odd(self):
        assert is_even(-3) is False

    def test_two(self):
        assert is_even(2) is True

    def test_one(self):
        assert is_even(1) is False

    def test_returns_bool(self):
        result = is_even(4)
        assert isinstance(result, bool), "is_even() must return True or False (a boolean)"


class TestIsOdd:
    def test_odd_number(self):
        assert is_odd(3) is True

    def test_even_number(self):
        assert is_odd(4) is False

    def test_zero_is_not_odd(self):
        assert is_odd(0) is False

    def test_negative_odd(self):
        assert is_odd(-3) is True

    def test_negative_even(self):
        assert is_odd(-4) is False

    def test_one_is_odd(self):
        assert is_odd(1) is True

    def test_returns_bool(self):
        result = is_odd(3)
        assert isinstance(result, bool), "is_odd() must return True or False (a boolean)"


class TestClassifyNumber:
    def test_even_returns_string_even(self):
        assert classify_number(6) == "even"

    def test_odd_returns_string_odd(self):
        assert classify_number(9) == "odd"

    def test_zero_is_even(self):
        assert classify_number(0) == "even"

    def test_negative_even(self):
        assert classify_number(-2) == "even"

    def test_negative_odd(self):
        assert classify_number(-3) == "odd"

    def test_returns_lowercase(self):
        result = classify_number(4)
        assert result == result.lower(), "Return lowercase 'even' or 'odd', not 'Even' or 'ODD'"

    def test_returns_string(self):
        result = classify_number(5)
        assert isinstance(result, str), "classify_number() must return a string: 'even' or 'odd'"
