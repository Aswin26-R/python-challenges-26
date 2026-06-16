import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import count_words, most_common_word, unique_words


class TestCountWords:
    def test_basic_count(self):
        result = count_words("hello world hello")
        assert result == {"hello": 2, "world": 1}

    def test_case_insensitive(self):
        result = count_words("The cat sat on the mat")
        assert result["the"] == 2, "'The' and 'the' should be counted together"

    def test_empty_string(self):
        result = count_words("")
        assert result == {}

    def test_single_word(self):
        result = count_words("hello")
        assert result == {"hello": 1}

    def test_returns_dict(self):
        result = count_words("hello world")
        assert isinstance(result, dict)

    def test_all_lowercase_keys(self):
        result = count_words("Hello WORLD")
        assert "hello" in result
        assert "world" in result
        assert "Hello" not in result
        assert "WORLD" not in result


class TestMostCommonWord:
    def test_basic(self):
        assert most_common_word("hello world hello python hello") == "hello"

    def test_the(self):
        assert most_common_word("the cat sat on the mat") == "the"

    def test_single_word(self):
        assert most_common_word("python") == "python"

    def test_case_insensitive(self):
        result = most_common_word("Hello HELLO hello world")
        assert result == "hello"

    def test_returns_string(self):
        result = most_common_word("a b a")
        assert isinstance(result, str)


class TestUniqueWords:
    def test_removes_duplicates(self):
        result = unique_words("banana apple banana cherry apple")
        assert result == ["apple", "banana", "cherry"]

    def test_sorted_alphabetically(self):
        result = unique_words("zebra apple mango")
        assert result == ["apple", "mango", "zebra"]

    def test_case_insensitive(self):
        result = unique_words("Hello hello HELLO")
        assert result == ["hello"]

    def test_empty_string(self):
        result = unique_words("")
        assert result == []

    def test_returns_list(self):
        result = unique_words("hello world")
        assert isinstance(result, list)

    def test_no_duplicates(self):
        result = unique_words("a a a b b c")
        assert len(result) == 3
