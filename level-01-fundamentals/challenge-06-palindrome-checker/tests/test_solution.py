import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import clean_string, is_palindrome


class TestCleanString:
    def test_lowercase(self):
        assert clean_string("HELLO") == "hello"

    def test_removes_spaces(self):
        assert clean_string("hello world") == "helloworld"

    def test_both(self):
        assert clean_string("Hello World") == "helloworld"

    def test_already_clean(self):
        assert clean_string("hello") == "hello"

    def test_empty(self):
        assert clean_string("") == ""

    def test_race_car(self):
        assert clean_string("Race Car") == "racecar"

    def test_returns_string(self):
        result = clean_string("Test")
        assert isinstance(result, str)


class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_case_insensitive(self):
        assert is_palindrome("Madam") is True

    def test_classic_phrase(self):
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_empty_string(self):
        assert is_palindrome("") is True

    def test_single_character(self):
        assert is_palindrome("a") is True

    def test_two_same_chars(self):
        assert is_palindrome("aa") is True

    def test_two_different_chars(self):
        assert is_palindrome("ab") is False

    def test_level(self):
        assert is_palindrome("level") is True

    def test_python(self):
        assert is_palindrome("python") is False

    def test_returns_bool(self):
        result = is_palindrome("racecar")
        assert isinstance(result, bool)
