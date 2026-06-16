import pytest
import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import async_greet, fetch_multiple, async_countdown, run_with_timeout


class TestAsyncGreet:
    def test_returns_greeting(self):
        result = asyncio.run(async_greet("Alice", 0))
        assert result == "Hello, Alice!"

    def test_different_names(self):
        result = asyncio.run(async_greet("Bob", 0))
        assert result == "Hello, Bob!"

    def test_returns_string(self):
        result = asyncio.run(async_greet("Test", 0))
        assert isinstance(result, str)

    def test_is_coroutine(self):
        import inspect
        assert inspect.iscoroutinefunction(async_greet)


class TestFetchMultiple:
    def test_returns_all_greetings(self):
        result = asyncio.run(fetch_multiple(["Alice", "Bob", "Charlie"], 0))
        assert result == ["Hello, Alice!", "Hello, Bob!", "Hello, Charlie!"]

    def test_order_preserved(self):
        names = ["Charlie", "Alice", "Bob"]
        result = asyncio.run(fetch_multiple(names, 0))
        assert result[0] == "Hello, Charlie!"
        assert result[1] == "Hello, Alice!"
        assert result[2] == "Hello, Bob!"

    def test_empty_list(self):
        result = asyncio.run(fetch_multiple([], 0))
        assert result == []

    def test_concurrent_faster_than_sequential(self):
        import time
        names = ["A", "B", "C"]
        delay = 0.05

        start = time.time()
        asyncio.run(fetch_multiple(names, delay))
        elapsed = time.time() - start

        assert elapsed < delay * 2, f"Should run concurrently — took {elapsed:.3f}s but expected < {delay*2:.3f}s"

    def test_returns_list(self):
        result = asyncio.run(fetch_multiple(["A"], 0))
        assert isinstance(result, list)


class TestAsyncCountdown:
    def test_countdown(self):
        async def collect():
            result = []
            async for n in async_countdown(5):
                result.append(n)
            return result
        result = asyncio.run(collect())
        assert result == [5, 4, 3, 2, 1]

    def test_countdown_one(self):
        async def collect():
            result = []
            async for n in async_countdown(1):
                result.append(n)
            return result
        assert asyncio.run(collect()) == [1]

    def test_countdown_zero(self):
        async def collect():
            result = []
            async for n in async_countdown(0):
                result.append(n)
            return result
        assert asyncio.run(collect()) == []


class TestRunWithTimeout:
    def test_fast_coro_succeeds(self):
        result = asyncio.run(run_with_timeout(async_greet("Alice", 0), timeout=1.0))
        assert result == "Hello, Alice!"

    def test_slow_coro_times_out(self):
        result = asyncio.run(run_with_timeout(async_greet("Alice", 5), timeout=0.05))
        assert result is None

    def test_timeout_returns_none(self):
        async def slow():
            await asyncio.sleep(10)
            return "done"
        result = asyncio.run(run_with_timeout(slow(), timeout=0.01))
        assert result is None
