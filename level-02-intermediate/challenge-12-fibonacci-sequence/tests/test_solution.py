import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import fibonacci, fibonacci_sequence


class TestFibonacci:
    def test_zero(self):
        assert fibonacci(0) == 0

    def test_one(self):
        assert fibonacci(1) == 1

    def test_two(self):
        assert fibonacci(2) == 1

    def test_three(self):
        assert fibonacci(3) == 2

    def test_four(self):
        assert fibonacci(4) == 3

    def test_five(self):
        assert fibonacci(5) == 5

    def test_six(self):
        assert fibonacci(6) == 8

    def test_seven(self):
        assert fibonacci(7) == 13

    def test_ten(self):
        assert fibonacci(10) == 55

    def test_returns_int(self):
        result = fibonacci(5)
        assert isinstance(result, int)


class TestFibonacciSequence:
    def test_five_numbers(self):
        assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]

    def test_ten_numbers(self):
        assert fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_one_number(self):
        assert fibonacci_sequence(1) == [0]

    def test_two_numbers(self):
        assert fibonacci_sequence(2) == [0, 1]

    def test_zero_count(self):
        assert fibonacci_sequence(0) == []

    def test_returns_list(self):
        result = fibonacci_sequence(5)
        assert isinstance(result, list)

    def test_correct_length(self):
        result = fibonacci_sequence(7)
        assert len(result) == 7

    def test_each_number_is_sum_of_previous_two(self):
        seq = fibonacci_sequence(8)
        for i in range(2, len(seq)):
            assert seq[i] == seq[i-1] + seq[i-2], f"seq[{i}] should equal seq[{i-1}] + seq[{i-2}]"
