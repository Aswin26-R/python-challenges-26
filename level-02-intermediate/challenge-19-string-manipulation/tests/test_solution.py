import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import title_case, count_vowels, remove_duplicates, truncate, is_anagram


class TestTitleCase:
    def test_basic(self):
        assert title_case("hello world") == "Hello World"

    def test_mixed_case_input(self):
        assert title_case("the QUICK brown FOX") == "The Quick Brown Fox"

    def test_empty(self):
        assert title_case("") == ""

    def test_single_word(self):
        assert title_case("python") == "Python"

    def test_returns_string(self):
        result = title_case("hello")
        assert isinstance(result, str)


class TestCountVowels:
    def test_hello_world(self):
        assert count_vowels("Hello World") == 3

    def test_no_vowels(self):
        assert count_vowels("rhythm") == 0

    def test_all_vowels(self):
        assert count_vowels("AEIOUaeiou") == 10

    def test_empty(self):
        assert count_vowels("") == 0

    def test_uppercase_vowels(self):
        assert count_vowels("AEIOU") == 5

    def test_returns_int(self):
        result = count_vowels("hello")
        assert isinstance(result, int)


class TestRemoveDuplicates:
    def test_basic(self):
        assert remove_duplicates("aabbcc") == "abc"

    def test_hello(self):
        assert remove_duplicates("hello") == "helo"

    def test_no_duplicates(self):
        assert remove_duplicates("abc") == "abc"

    def test_non_consecutive(self):
        assert remove_duplicates("aabba") == "aba"

    def test_empty(self):
        assert remove_duplicates("") == ""

    def test_single_char(self):
        assert remove_duplicates("a") == "a"

    def test_all_same(self):
        assert remove_duplicates("aaaa") == "a"


class TestTruncate:
    def test_truncation(self):
        assert truncate("Hello World", 8) == "Hello..."

    def test_no_truncation(self):
        assert truncate("Hi", 10) == "Hi"

    def test_exact_length(self):
        assert truncate("Hello", 5) == "Hello"

    def test_one_over(self):
        assert truncate("Hello!", 5) == "He..."

    def test_short_max(self):
        assert truncate("Hello World", 5) == "He..."

    def test_returns_string(self):
        result = truncate("test", 10)
        assert isinstance(result, str)


class TestIsAnagram:
    def test_listen_silent(self):
        assert is_anagram("listen", "silent") is True

    def test_not_anagram(self):
        assert is_anagram("hello", "world") is False

    def test_same_word(self):
        assert is_anagram("abc", "abc") is True

    def test_different_order(self):
        assert is_anagram("abc", "cba") is True

    def test_case_insensitive(self):
        assert is_anagram("Listen", "Silent") is True

    def test_with_spaces(self):
        assert is_anagram("Astronomer", "Moon starer") is True

    def test_returns_bool(self):
        result = is_anagram("abc", "cba")
        assert isinstance(result, bool)
