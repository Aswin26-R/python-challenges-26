import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import fizzbuzz, fizzbuzz_list


class TestFizzBuzz:
    def test_returns_string(self):
        result = fizzbuzz(1)
        assert isinstance(result, str), "fizzbuzz() must return a string"

    def test_number_one(self):
        assert fizzbuzz(1) == "1"

    def test_number_two(self):
        assert fizzbuzz(2) == "2"

    def test_fizz_three(self):
        assert fizzbuzz(3) == "Fizz"

    def test_number_four(self):
        assert fizzbuzz(4) == "4"

    def test_buzz_five(self):
        assert fizzbuzz(5) == "Buzz"

    def test_fizz_six(self):
        assert fizzbuzz(6) == "Fizz"

    def test_number_seven(self):
        assert fizzbuzz(7) == "7"

    def test_fizz_nine(self):
        assert fizzbuzz(9) == "Fizz"

    def test_buzz_ten(self):
        assert fizzbuzz(10) == "Buzz"

    def test_fizzbuzz_fifteen(self):
        assert fizzbuzz(15) == "FizzBuzz", "15 is divisible by both 3 and 5 — should return 'FizzBuzz'"

    def test_fizzbuzz_thirty(self):
        assert fizzbuzz(30) == "FizzBuzz"

    def test_fizz_twelve(self):
        assert fizzbuzz(12) == "Fizz"

    def test_buzz_twenty(self):
        assert fizzbuzz(20) == "Buzz"

    def test_number_as_string_not_int(self):
        result = fizzbuzz(7)
        assert result == "7", "Regular numbers must be returned as strings, not integers"


class TestFizzBuzzList:
    def test_one_to_five(self):
        expected = ["1", "2", "Fizz", "4", "Buzz"]
        assert fizzbuzz_list(1, 5) == expected

    def test_one_to_fifteen(self):
        expected = [
            "1", "2", "Fizz", "4", "Buzz",
            "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz"
        ]
        assert fizzbuzz_list(1, 15) == expected

    def test_single_number_fizzbuzz(self):
        assert fizzbuzz_list(15, 15) == ["FizzBuzz"]

    def test_single_number_regular(self):
        assert fizzbuzz_list(1, 1) == ["1"]

    def test_range_around_fizzbuzz(self):
        assert fizzbuzz_list(13, 16) == ["13", "14", "FizzBuzz", "16"]

    def test_returns_list(self):
        result = fizzbuzz_list(1, 5)
        assert isinstance(result, list), "fizzbuzz_list() must return a list"

    def test_correct_length(self):
        result = fizzbuzz_list(1, 10)
        assert len(result) == 10, "List should have one entry per number in range"
