import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import is_prime, get_primes


class TestIsPrime:
    def test_two_is_prime(self):
        assert is_prime(2) is True

    def test_three_is_prime(self):
        assert is_prime(3) is True

    def test_four_is_not_prime(self):
        assert is_prime(4) is False

    def test_seventeen_is_prime(self):
        assert is_prime(17) is True

    def test_one_is_not_prime(self):
        assert is_prime(1) is False, "1 is not a prime number by definition"

    def test_zero_is_not_prime(self):
        assert is_prime(0) is False

    def test_negative_is_not_prime(self):
        assert is_prime(-5) is False

    def test_prime_11(self):
        assert is_prime(11) is True

    def test_prime_13(self):
        assert is_prime(13) is True

    def test_not_prime_9(self):
        assert is_prime(9) is False

    def test_not_prime_25(self):
        assert is_prime(25) is False

    def test_prime_97(self):
        assert is_prime(97) is True

    def test_not_prime_100(self):
        assert is_prime(100) is False

    def test_returns_bool(self):
        result = is_prime(7)
        assert isinstance(result, bool)


class TestGetPrimes:
    def test_primes_to_10(self):
        assert get_primes(10) == [2, 3, 5, 7]

    def test_primes_to_20(self):
        assert get_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    def test_primes_to_2(self):
        assert get_primes(2) == [2]

    def test_primes_to_1(self):
        assert get_primes(1) == []

    def test_primes_to_0(self):
        assert get_primes(0) == []

    def test_returns_list(self):
        result = get_primes(10)
        assert isinstance(result, list)

    def test_all_results_are_prime(self):
        primes = get_primes(50)
        for p in primes:
            assert is_prime(p), f"{p} should be prime"

    def test_count_of_primes_to_30(self):
        result = get_primes(30)
        assert len(result) == 10
