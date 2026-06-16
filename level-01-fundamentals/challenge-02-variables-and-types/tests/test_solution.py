import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import get_type_name, is_integer, is_string, convert_to_int, convert_to_string, add_numbers


class TestGetTypeName:
    def test_int_type(self):
        assert get_type_name(42) == "int"

    def test_float_type(self):
        assert get_type_name(3.14) == "float"

    def test_str_type(self):
        assert get_type_name("hello") == "str"

    def test_bool_type(self):
        assert get_type_name(True) == "bool"

    def test_zero_is_int(self):
        assert get_type_name(0) == "int"

    def test_returns_string(self):
        result = get_type_name(42)
        assert isinstance(result, str), "get_type_name() must return a string"


class TestIsInteger:
    def test_positive_int(self):
        assert is_integer(5) is True

    def test_negative_int(self):
        assert is_integer(-3) is True

    def test_zero(self):
        assert is_integer(0) is True

    def test_float_is_not_int(self):
        assert is_integer(5.0) is False

    def test_string_is_not_int(self):
        assert is_integer("5") is False

    def test_bool_is_not_int(self):
        assert is_integer(True) is False, "True is technically a bool, not an int — return False for booleans"

    def test_none_is_not_int(self):
        assert is_integer(None) is False


class TestIsString:
    def test_basic_string(self):
        assert is_string("hello") is True

    def test_empty_string(self):
        assert is_string("") is True

    def test_number_is_not_string(self):
        assert is_string(123) is False

    def test_bool_is_not_string(self):
        assert is_string(True) is False

    def test_none_is_not_string(self):
        assert is_string(None) is False


class TestConvertToInt:
    def test_string_to_int(self):
        assert convert_to_int("42") == 42

    def test_float_to_int_truncates(self):
        assert convert_to_int(3.9) == 3

    def test_negative_string(self):
        assert convert_to_int("-7") == -7

    def test_returns_int_type(self):
        result = convert_to_int("10")
        assert isinstance(result, int), "convert_to_int() must return an int"


class TestConvertToString:
    def test_int_to_string(self):
        assert convert_to_string(99) == "99"

    def test_float_to_string(self):
        assert convert_to_string(3.14) == "3.14"

    def test_bool_to_string(self):
        assert convert_to_string(True) == "True"

    def test_returns_str_type(self):
        result = convert_to_string(42)
        assert isinstance(result, str), "convert_to_string() must return a string"


class TestAddNumbers:
    def test_add_integers(self):
        assert add_numbers(3, 4) == 7

    def test_add_floats(self):
        assert add_numbers(1.5, 2.5) == 4.0

    def test_add_negative(self):
        assert add_numbers(-1, 1) == 0

    def test_add_zeros(self):
        assert add_numbers(0, 0) == 0
