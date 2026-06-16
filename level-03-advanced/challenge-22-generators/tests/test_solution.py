import pytest
import sys
import os
import types

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import count_up, fibonacci_generator, take, squares_generator


class TestCountUp:
    def test_basic_range(self):
        assert list(count_up(1, 5)) == [1, 2, 3, 4, 5]

    def test_single_value(self):
        assert list(count_up(3, 3)) == [3]

    def test_from_zero(self):
        assert list(count_up(0, 3)) == [0, 1, 2, 3]

    def test_is_generator(self):
        gen = count_up(1, 5)
        assert isinstance(gen, types.GeneratorType), "count_up() must return a generator, not a list"

    def test_next_works(self):
        gen = count_up(10, 15)
        assert next(gen) == 10
        assert next(gen) == 11


class TestFibonacciGenerator:
    def test_first_values(self):
        fib = fibonacci_generator()
        assert next(fib) == 0
        assert next(fib) == 1
        assert next(fib) == 1
        assert next(fib) == 2
        assert next(fib) == 3

    def test_is_generator(self):
        fib = fibonacci_generator()
        assert isinstance(fib, types.GeneratorType), "fibonacci_generator() must return a generator"

    def test_first_ten(self):
        fib = fibonacci_generator()
        result = [next(fib) for _ in range(10)]
        assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


class TestTake:
    def test_take_from_count_up(self):
        assert take(count_up(1, 100), 3) == [1, 2, 3]

    def test_take_from_fibonacci(self):
        fib = fibonacci_generator()
        assert take(fib, 5) == [0, 1, 1, 2, 3]

    def test_continues_from_position(self):
        fib = fibonacci_generator()
        take(fib, 5)            # consume first 5
        result = take(fib, 3)   # get next 3
        assert result == [5, 8, 13]

    def test_take_returns_list(self):
        result = take(count_up(1, 10), 3)
        assert isinstance(result, list)

    def test_take_zero(self):
        result = take(count_up(1, 10), 0)
        assert result == []


class TestSquaresGenerator:
    def test_basic(self):
        assert list(squares_generator(30)) == [1, 4, 9, 16, 25]

    def test_limit_one(self):
        assert list(squares_generator(1)) == [1]

    def test_limit_zero(self):
        assert list(squares_generator(0)) == []

    def test_includes_limit(self):
        assert list(squares_generator(100)) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    def test_is_generator(self):
        gen = squares_generator(10)
        assert isinstance(gen, types.GeneratorType), "squares_generator() must return a generator"
