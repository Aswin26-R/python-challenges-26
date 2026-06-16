import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import safe_divide, safe_int_convert, get_list_item, validate_age


class TestSafeDivide:
    def test_basic_division(self):
        assert safe_divide(10, 2) == 5.0

    def test_divide_by_zero_returns_none(self):
        result = safe_divide(10, 0)
        assert result is None, "Division by zero should return None, not raise an exception"

    def test_decimal_result(self):
        assert safe_divide(7, 2) == 3.5

    def test_zero_numerator(self):
        assert safe_divide(0, 5) == 0.0

    def test_does_not_raise(self):
        try:
            safe_divide(1, 0)
        except ZeroDivisionError:
            pytest.fail("safe_divide() raised ZeroDivisionError — it should return None instead")


class TestSafeIntConvert:
    def test_string_number(self):
        assert safe_int_convert("42") == 42

    def test_invalid_string(self):
        result = safe_int_convert("hello")
        assert result is None

    def test_float_to_int(self):
        assert safe_int_convert(3.7) == 3

    def test_none_input(self):
        result = safe_int_convert(None)
        assert result is None

    def test_does_not_raise(self):
        try:
            result = safe_int_convert("abc")
        except (ValueError, TypeError):
            pytest.fail("safe_int_convert() raised an exception — it should return None")

    def test_negative_string(self):
        assert safe_int_convert("-5") == -5


class TestGetListItem:
    def test_valid_index(self):
        assert get_list_item([10, 20, 30], 1) == 20

    def test_out_of_range_returns_none(self):
        result = get_list_item([10, 20, 30], 99)
        assert result is None

    def test_empty_list(self):
        result = get_list_item([], 0)
        assert result is None

    def test_negative_index(self):
        assert get_list_item([10, 20, 30], -1) == 30

    def test_does_not_raise(self):
        try:
            get_list_item([1, 2], 100)
        except IndexError:
            pytest.fail("get_list_item() raised IndexError — it should return None")


class TestValidateAge:
    def test_valid_age(self):
        assert validate_age(25) is True

    def test_zero_is_valid(self):
        assert validate_age(0) is True

    def test_150_is_valid(self):
        assert validate_age(150) is True

    def test_negative_raises_value_error(self):
        with pytest.raises(ValueError):
            validate_age(-1)

    def test_too_high_raises_value_error(self):
        with pytest.raises(ValueError):
            validate_age(200)

    def test_error_message(self):
        with pytest.raises(ValueError, match="Age must be between 0 and 150"):
            validate_age(-5)
