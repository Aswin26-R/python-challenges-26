import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import apply_to_all, keep_if, reduce_list, pipeline, compose


class TestApplyToAll:
    def test_double(self):
        assert apply_to_all(lambda x: x * 2, [1, 2, 3, 4]) == [2, 4, 6, 8]

    def test_str_conversion(self):
        assert apply_to_all(str, [1, 2, 3]) == ["1", "2", "3"]

    def test_empty_list(self):
        assert apply_to_all(lambda x: x * 2, []) == []

    def test_squares(self):
        assert apply_to_all(lambda x: x ** 2, [1, 2, 3]) == [1, 4, 9]

    def test_returns_list(self):
        result = apply_to_all(lambda x: x, [1, 2])
        assert isinstance(result, list)


class TestKeepIf:
    def test_filter_greater_than(self):
        assert keep_if(lambda x: x > 3, [1, 2, 3, 4, 5, 6]) == [4, 5, 6]

    def test_filter_evens(self):
        assert keep_if(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    def test_filter_strings(self):
        result = keep_if(lambda s: len(s) > 3, ["hi", "hello", "hey"])
        assert result == ["hello"]

    def test_empty_list(self):
        assert keep_if(lambda x: x > 0, []) == []

    def test_none_pass(self):
        assert keep_if(lambda x: x > 100, [1, 2, 3]) == []

    def test_returns_list(self):
        result = keep_if(lambda x: True, [1, 2])
        assert isinstance(result, list)


class TestReduceList:
    def test_sum(self):
        assert reduce_list(lambda acc, x: acc + x, [1, 2, 3, 4, 5], 0) == 15

    def test_product(self):
        assert reduce_list(lambda acc, x: acc * x, [1, 2, 3, 4], 1) == 24

    def test_max(self):
        assert reduce_list(lambda acc, x: acc if acc > x else x, [3, 1, 4, 1, 5, 9], 0) == 9

    def test_string_join(self):
        result = reduce_list(lambda acc, x: acc + x, ["a", "b", "c"], "")
        assert result == "abc"

    def test_empty_list_returns_initial(self):
        assert reduce_list(lambda acc, x: acc + x, [], 99) == 99


class TestPipeline:
    def test_basic_pipeline(self):
        result = pipeline(5, lambda x: x * 2, lambda x: x + 1, lambda x: x ** 2)
        assert result == 121

    def test_single_function(self):
        assert pipeline(5, lambda x: x * 2) == 10

    def test_no_functions(self):
        assert pipeline(42) == 42

    def test_string_pipeline(self):
        result = pipeline("hello", str.upper, lambda s: s + "!")
        assert result == "HELLO!"

    def test_order_matters(self):
        r1 = pipeline(5, lambda x: x + 1, lambda x: x * 2)  # (5+1)*2 = 12
        r2 = pipeline(5, lambda x: x * 2, lambda x: x + 1)  # (5*2)+1 = 11
        assert r1 == 12
        assert r2 == 11


class TestCompose:
    def test_add_then_double(self):
        add_one = lambda x: x + 1
        double = lambda x: x * 2
        add_then_double = compose(double, add_one)
        assert add_then_double(5) == 12  # (5+1)*2

    def test_double_then_add(self):
        add_one = lambda x: x + 1
        double = lambda x: x * 2
        double_then_add = compose(add_one, double)
        assert double_then_add(5) == 11  # (5*2)+1

    def test_compose_returns_callable(self):
        f = compose(lambda x: x + 1, lambda x: x * 2)
        assert callable(f)

    def test_compose_strings(self):
        upper_exclaim = compose(lambda s: s + "!", str.upper)
        assert upper_exclaim("hello") == "HELLO!"
