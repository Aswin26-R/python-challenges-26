import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import greet, describe_yourself, format_greeting


class TestGreet:
    def test_greet_returns_string(self):
        result = greet("Alice")
        assert isinstance(result, str), "greet() must return a string"

    def test_greet_basic(self):
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_another_name(self):
        assert greet("Bob") == "Hello, Bob!"

    def test_greet_single_name(self):
        assert greet("X") == "Hello, X!"

    def test_greet_full_name(self):
        assert greet("John Smith") == "Hello, John Smith!"

    def test_greet_not_none(self):
        result = greet("Test")
        assert result is not None, "greet() must return a value, not None. Did you use 'return'?"


class TestDescribeYourself:
    def test_describe_returns_string(self):
        result = describe_yourself("Alice", "developer")
        assert isinstance(result, str), "describe_yourself() must return a string"

    def test_describe_basic(self):
        result = describe_yourself("Maria", "software engineer")
        assert result == "My name is Maria and I am a software engineer."

    def test_describe_different_role(self):
        result = describe_yourself("John", "student")
        assert result == "My name is John and I am a student."

    def test_describe_ends_with_period(self):
        result = describe_yourself("Alice", "developer")
        assert result.endswith("."), "The sentence must end with a period (.)"

    def test_describe_not_none(self):
        result = describe_yourself("Test", "tester")
        assert result is not None, "describe_yourself() must return a value. Did you use 'return'?"


class TestFormatGreeting:
    def test_format_returns_string(self):
        result = format_greeting("Hello", "World")
        assert isinstance(result, str), "format_greeting() must return a string"

    def test_format_basic(self):
        assert format_greeting("Hi", "World") == "Hi, World!"

    def test_format_good_morning(self):
        assert format_greeting("Good morning", "Carlos") == "Good morning, Carlos!"

    def test_format_has_comma(self):
        result = format_greeting("Hey", "Alice")
        assert ", " in result, "There must be a comma and space between greeting and name"

    def test_format_ends_with_exclamation(self):
        result = format_greeting("Hello", "Test")
        assert result.endswith("!"), "The greeting must end with an exclamation mark (!)"

    def test_format_not_none(self):
        result = format_greeting("Hi", "Test")
        assert result is not None, "format_greeting() must return a value. Did you use 'return'?"
