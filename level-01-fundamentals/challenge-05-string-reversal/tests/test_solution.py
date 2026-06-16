import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import reverse_string, reverse_words


class TestReverseString:
    def test_basic_reverse(self):
        assert reverse_string("hello") == "olleh"

    def test_python_reverse(self):
        assert reverse_string("Python") == "nohtyP"

    def test_empty_string(self):
        assert reverse_string("") == ""

    def test_single_character(self):
        assert reverse_string("a") == "a"

    def test_numbers_as_string(self):
        assert reverse_string("12345") == "54321"

    def test_palindrome_unchanged(self):
        assert reverse_string("racecar") == "racecar"

    def test_spaces_included(self):
        assert reverse_string("ab cd") == "dc ba"

    def test_returns_string(self):
        result = reverse_string("test")
        assert isinstance(result, str), "reverse_string() must return a string"

    def test_not_original(self):
        original = "hello"
        result = reverse_string(original)
        assert result != original, "reverse_string('hello') should NOT equal 'hello'"


class TestReverseWords:
    def test_two_words(self):
        assert reverse_words("hello world") == "world hello"

    def test_three_words(self):
        assert reverse_words("I love Python") == "Python love I"

    def test_single_word(self):
        assert reverse_words("one") == "one"

    def test_abc(self):
        assert reverse_words("a b c") == "c b a"

    def test_four_words(self):
        assert reverse_words("one two three four") == "four three two one"

    def test_returns_string(self):
        result = reverse_words("hello world")
        assert isinstance(result, str), "reverse_words() must return a string"

    def test_single_space_between_words(self):
        result = reverse_words("hello world")
        assert "  " not in result, "Words should be separated by a single space"
