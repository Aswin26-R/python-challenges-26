import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import add, subtract, multiply, divide, calculate


class TestAdd:
    def test_basic_addition(self):
        assert add(3, 4) == 7

    def test_add_negatives(self):
        assert add(-1, -1) == -2

    def test_add_zero(self):
        assert add(0, 0) == 0

    def test_add_positive_negative(self):
        assert add(-1, 1) == 0

    def test_add_floats(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    def test_basic_subtraction(self):
        assert subtract(10, 3) == 7

    def test_subtract_to_negative(self):
        assert subtract(0, 5) == -5

    def test_subtract_same(self):
        assert subtract(5, 5) == 0

    def test_subtract_negatives(self):
        assert subtract(-3, -1) == -2


class TestMultiply:
    def test_basic_multiplication(self):
        assert multiply(4, 5) == 20

    def test_multiply_negative(self):
        assert multiply(-2, 3) == -6

    def test_multiply_by_zero(self):
        assert multiply(0, 99) == 0

    def test_multiply_by_one(self):
        assert multiply(7, 1) == 7

    def test_two_negatives(self):
        assert multiply(-2, -3) == 6


class TestDivide:
    def test_basic_division(self):
        assert divide(10, 2) == 5.0

    def test_division_with_decimal(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_returns_none(self):
        result = divide(10, 0)
        assert result is None, "divide(10, 0) must return None, not raise an exception"

    def test_zero_divided_by_number(self):
        assert divide(0, 5) == 0.0

    def test_returns_float(self):
        result = divide(10, 2)
        assert isinstance(result, float), "divide() should return a float"


class TestCalculate:
    def test_addition(self):
        assert calculate(3, "+", 4) == 7

    def test_subtraction(self):
        assert calculate(10, "-", 3) == 7

    def test_multiplication(self):
        assert calculate(4, "*", 5) == 20

    def test_division(self):
        assert calculate(10, "/", 2) == 5.0

    def test_division_by_zero(self):
        result = calculate(10, "/", 0)
        assert result is None

    def test_unknown_operator(self):
        result = calculate(5, "@", 2)
        assert result is None, "Unknown operators should return None"

    def test_negative_numbers(self):
        assert calculate(-5, "+", 3) == -2

    def test_calculate_with_floats(self):
        assert calculate(1.5, "+", 2.5) == 4.0
