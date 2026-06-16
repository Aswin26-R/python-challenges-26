import pytest
import time
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import memoize, fibonacci_naive, fibonacci_cached, Cache


class TestMemoize:
    def test_returns_correct_result(self):
        @memoize
        def add(a, b):
            return a + b
        assert add(2, 3) == 5

    def test_caches_result(self):
        call_count = [0]

        @memoize
        def expensive(n):
            call_count[0] += 1
            return n * 2

        expensive(5)
        expensive(5)
        expensive(5)
        assert call_count[0] == 1, "Function should only be called once for same args"

    def test_different_args_not_cached(self):
        call_count = [0]

        @memoize
        def fn(n):
            call_count[0] += 1
            return n

        fn(1)
        fn(2)
        assert call_count[0] == 2

    def test_returns_correct_for_multiple_args(self):
        @memoize
        def multiply(a, b):
            return a * b
        assert multiply(3, 4) == 12
        assert multiply(5, 6) == 30


class TestFibonacciNaive:
    def test_base_cases(self):
        assert fibonacci_naive(0) == 0
        assert fibonacci_naive(1) == 1

    def test_known_values(self):
        assert fibonacci_naive(5) == 5
        assert fibonacci_naive(10) == 55

    def test_sequence(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, val in enumerate(expected):
            assert fibonacci_naive(i) == val


class TestFibonacciCached:
    def test_base_cases(self):
        assert fibonacci_cached(0) == 0
        assert fibonacci_cached(1) == 1

    def test_known_values(self):
        assert fibonacci_cached(10) == 55
        assert fibonacci_cached(20) == 6765

    def test_large_value_fast(self):
        start = time.time()
        result = fibonacci_cached(50)
        elapsed = time.time() - start
        assert result == 12586269025
        assert elapsed < 1.0, "Cached fibonacci should be very fast"

    def test_faster_than_naive(self):
        n = 30
        start = time.time()
        fibonacci_naive(n)
        naive_time = time.time() - start

        fibonacci_cached.cache_clear()
        start = time.time()
        fibonacci_cached(n)
        cached_time = time.time() - start

        assert cached_time <= naive_time


class TestCache:
    def test_set_and_get(self):
        cache = Cache()
        cache.set("key", "value")
        assert cache.get("key") == "value"

    def test_get_missing_returns_none(self):
        cache = Cache()
        assert cache.get("missing") is None

    def test_evicts_oldest(self):
        cache = Cache(max_size=2)
        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("c", 3)  # "a" evicted
        assert cache.get("a") is None
        assert cache.get("b") == 2
        assert cache.get("c") == 3

    def test_update_existing_no_eviction(self):
        cache = Cache(max_size=2)
        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("a", 99)  # update, no eviction
        assert cache.get("a") == 99
        assert cache.get("b") == 2

    def test_delete(self):
        cache = Cache()
        cache.set("x", 10)
        cache.delete("x")
        assert cache.get("x") is None

    def test_clear(self):
        cache = Cache()
        cache.set("a", 1)
        cache.set("b", 2)
        cache.clear()
        assert cache.size() == 0

    def test_size(self):
        cache = Cache()
        assert cache.size() == 0
        cache.set("a", 1)
        assert cache.size() == 1
        cache.set("b", 2)
        assert cache.size() == 2

    def test_max_size_respected(self):
        cache = Cache(max_size=3)
        for i in range(10):
            cache.set(str(i), i)
        assert cache.size() == 3
