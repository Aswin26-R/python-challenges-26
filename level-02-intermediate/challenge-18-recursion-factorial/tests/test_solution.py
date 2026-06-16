import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import factorial_recursive, factorial_iterative, count_down


class TestFactorialRecursive:
    def test_zero(self):
        assert factorial_recursive(0) == 1

    def test_one(self):
        assert factorial_recursive(1) == 1

    def test_five(self):
        assert factorial_recursive(5) == 120

    def test_ten(self):
        assert factorial_recursive(10) == 3628800

    def test_two(self):
        assert factorial_recursive(2) == 2

    def test_three(self):
        assert factorial_recursive(3) == 6

    def test_four(self):
        assert factorial_recursive(4) == 24

    def test_returns_int(self):
        result = factorial_recursive(5)
        assert isinstance(result, int)


class TestFactorialIterative:
    def test_zero(self):
        assert factorial_iterative(0) == 1

    def test_one(self):
        assert factorial_iterative(1) == 1

    def test_five(self):
        assert factorial_iterative(5) == 120

    def test_ten(self):
        assert factorial_iterative(10) == 3628800

    def test_matches_recursive(self):
        for n in range(8):
            assert factorial_iterative(n) == factorial_recursive(n), \
                f"factorial_iterative({n}) should equal factorial_recursive({n})"


class TestCountDown:
    def test_five(self):
        assert count_down(5) == [5, 4, 3, 2, 1]

    def test_three(self):
        assert count_down(3) == [3, 2, 1]

    def test_one(self):
        assert count_down(1) == [1]

    def test_zero(self):
        assert count_down(0) == []

    def test_returns_list(self):
        result = count_down(3)
        assert isinstance(result, list)

    def test_descending_order(self):
        result = count_down(5)
        for i in range(len(result) - 1):
            assert result[i] > result[i+1], "List must be in descending order"
