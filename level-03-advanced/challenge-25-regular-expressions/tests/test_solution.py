import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import is_valid_email, extract_numbers, is_valid_phone, replace_whitespace, extract_hashtags


class TestIsValidEmail:
    def test_valid_basic(self):
        assert is_valid_email("user@example.com") is True

    def test_valid_with_dot(self):
        assert is_valid_email("user.name@domain.org") is True

    def test_no_at_symbol(self):
        assert is_valid_email("not-an-email") is False

    def test_no_domain_extension(self):
        assert is_valid_email("user@domain") is False

    def test_nothing_before_at(self):
        assert is_valid_email("@domain.com") is False

    def test_valid_plus_addressing(self):
        assert is_valid_email("user+filter@example.com") is True

    def test_returns_bool(self):
        result = is_valid_email("test@test.com")
        assert isinstance(result, bool)


class TestExtractNumbers:
    def test_basic(self):
        assert extract_numbers("I have 3 cats and 12 dogs") == ["3", "12"]

    def test_with_dollar_sign(self):
        assert extract_numbers("Worth $450 and 2 days") == ["450", "2"]

    def test_no_numbers(self):
        assert extract_numbers("No numbers here") == []

    def test_multiple_numbers(self):
        result = extract_numbers("Room 101 at 9pm floor 3")
        assert result == ["101", "9", "3"]

    def test_returns_list(self):
        result = extract_numbers("1 and 2")
        assert isinstance(result, list)

    def test_returns_strings(self):
        result = extract_numbers("42 items")
        assert all(isinstance(x, str) for x in result)


class TestIsValidPhone:
    def test_valid_phone(self):
        assert is_valid_phone("+91-987-654-3210") is True

    def test_no_plus(self):
        assert is_valid_phone("91-987-654-3210") is False

    def test_plain_digits(self):
        assert is_valid_phone("1234567890") is False

    def test_wrong_format(self):
        assert is_valid_phone("+91-98-654-3210") is False

    def test_returns_bool(self):
        result = is_valid_phone("+91-987-654-3210")
        assert isinstance(result, bool)


class TestReplaceWhitespace:
    def test_multiple_spaces(self):
        assert replace_whitespace("hello   world") == "hello world"

    def test_tabs(self):
        assert replace_whitespace("hello\t\tworld") == "hello world"

    def test_mixed(self):
        assert replace_whitespace("a  b\t\tc") == "a b c"

    def test_no_extra_spaces(self):
        assert replace_whitespace("no extra spaces") == "no extra spaces"

    def test_single_space_unchanged(self):
        assert replace_whitespace("a b c") == "a b c"

    def test_returns_string(self):
        result = replace_whitespace("a  b")
        assert isinstance(result, str)


class TestExtractHashtags:
    def test_basic(self):
        result = extract_hashtags("I love #python and #coding is #fun")
        assert result == ["#python", "#coding", "#fun"]

    def test_no_hashtags(self):
        assert extract_hashtags("No hashtags here") == []

    def test_single_hashtag(self):
        assert extract_hashtags("#hello") == ["#hello"]

    def test_returns_list(self):
        result = extract_hashtags("#test")
        assert isinstance(result, list)

    def test_hashtag_with_numbers(self):
        result = extract_hashtags("#python3 is #great")
        assert "#python3" in result
