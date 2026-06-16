import pytest
import time
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import timer, logger, validate_positive


class TestTimer:
    def test_returns_original_result(self):
        @timer
        def add(a, b):
            return a + b

        result = add(2, 3)
        assert result == 5

    def test_prints_timing(self, capsys):
        @timer
        def fast():
            return 42

        fast()
        captured = capsys.readouterr()
        assert "fast" in captured.out
        assert "seconds" in captured.out

    def test_preserves_function_name(self):
        @timer
        def my_function():
            return True

        assert my_function.__name__ == "my_function"

    def test_works_with_args(self):
        @timer
        def multiply(a, b):
            return a * b

        result = multiply(3, 4)
        assert result == 12


class TestLogger:
    def test_returns_original_result(self):
        @logger
        def add(a, b):
            return a + b

        result = add(3, 4)
        assert result == 7

    def test_prints_call_info(self, capsys):
        @logger
        def add(a, b):
            return a + b

        add(3, 4)
        captured = capsys.readouterr()
        assert "add" in captured.out
        assert "3" in captured.out
        assert "4" in captured.out

    def test_prints_return_value(self, capsys):
        @logger
        def add(a, b):
            return a + b

        add(3, 4)
        captured = capsys.readouterr()
        assert "7" in captured.out

    def test_preserves_function_name(self):
        @logger
        def my_func():
            return None

        assert my_func.__name__ == "my_func"


class TestValidatePositive:
    def test_positive_args_work(self):
        @validate_positive
        def multiply(a, b):
            return a * b

        assert multiply(3, 4) == 12

    def test_negative_raises(self):
        @validate_positive
        def add(a, b):
            return a + b

        with pytest.raises(ValueError, match="positive"):
            add(-1, 4)

    def test_zero_raises(self):
        @validate_positive
        def add(a, b):
            return a + b

        with pytest.raises(ValueError):
            add(0, 5)

    def test_preserves_function_name(self):
        @validate_positive
        def my_func(x):
            return x

        assert my_func.__name__ == "my_func"

    def test_single_negative_raises(self):
        @validate_positive
        def square(x):
            return x * x

        with pytest.raises(ValueError):
            square(-3)
