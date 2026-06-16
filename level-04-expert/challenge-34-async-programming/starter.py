import asyncio


async def async_greet(name, delay=0):
    """
    TODO:
    An async function that waits for 'delay' seconds, then returns a greeting.

    Examples (run with asyncio.run()):
        asyncio.run(async_greet("Alice", 0))   → "Hello, Alice!"
        asyncio.run(async_greet("Bob", 0.1))   → "Hello, Bob!" (after 0.1 seconds)

    Hint:
        async def async_greet(name, delay=0):
            await asyncio.sleep(delay)
            return f"Hello, {name}!"
    """
    pass


async def fetch_multiple(names, delay=0):
    """
    TODO:
    Fetch greetings for ALL names CONCURRENTLY using asyncio.gather().
    Return a list of greetings in the same order as the input names.

    The key point: all greetings should be fetched AT THE SAME TIME,
    not one by one. This is much faster when delay > 0.

    Example:
        asyncio.run(fetch_multiple(["Alice", "Bob", "Charlie"], 0))
        → ["Hello, Alice!", "Hello, Bob!", "Hello, Charlie!"]

    Hint:
        coroutines = [async_greet(name, delay) for name in names]
        results = await asyncio.gather(*coroutines)
        return list(results)
    """
    pass


async def async_countdown(start):
    """
    TODO:
    An async GENERATOR that counts down from 'start' to 1.
    Yield each number with a tiny delay.

    Example:
        async for n in async_countdown(3):
            print(n)
        # Prints: 3, 2, 1

    Hint:
        for i in range(start, 0, -1):
            await asyncio.sleep(0)   ← yield control briefly
            yield i
    """
    pass


async def run_with_timeout(coro, timeout):
    """
    TODO:
    Run the coroutine 'coro' with a time limit.
    If the coroutine finishes in time, return its result.
    If it takes longer than 'timeout' seconds, return None.

    Example:
        # Quick coroutine — finishes in time:
        result = asyncio.run(run_with_timeout(async_greet("Alice", 0), timeout=1.0))
        → "Hello, Alice!"

        # Slow coroutine — times out:
        result = asyncio.run(run_with_timeout(async_greet("Bob", 5), timeout=0.01))
        → None

    Hint:
        try:
            return await asyncio.wait_for(coro, timeout=timeout)
        except asyncio.TimeoutError:
            return None
    """
    pass
