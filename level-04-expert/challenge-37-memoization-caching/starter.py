import functools
import time


def memoize(func):
    """
    TODO:
    A decorator that caches the results of a function by its arguments.
    On repeated calls with the same arguments, return the cached result
    without re-executing the function.

    Example:
        @memoize
        def add(a, b):
            return a + b

        add(1, 2)   # computed normally → 3
        add(1, 2)   # returned from cache → 3 (no recomputation)
        add(3, 4)   # new args, computed → 7

    Implementation:
        cache = {}

        @functools.wraps(func)
        def wrapper(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]

        wrapper.cache = cache  ← expose cache for inspection in tests
        return wrapper
    """
    pass


def fibonacci_naive(n):
    """
    TODO:
    Naive recursive Fibonacci — NO caching.
    Extremely slow for large n (exponential time).

    Base cases: fibonacci_naive(0) = 0, fibonacci_naive(1) = 1
    Recursive: fibonacci_naive(n) = fibonacci_naive(n-1) + fibonacci_naive(n-2)

    Example:
        fibonacci_naive(0) → 0
        fibonacci_naive(1) → 1
        fibonacci_naive(10) → 55
    """
    pass


@functools.lru_cache(maxsize=None)
def fibonacci_cached(n):
    """
    TODO:
    Fibonacci with lru_cache — instant even for large n.
    Same logic as fibonacci_naive, but @functools.lru_cache handles caching.

    The @functools.lru_cache decorator is ALREADY applied above.
    You just need to implement the same recursive logic as fibonacci_naive.

    Example:
        fibonacci_cached(50) → 12586269025  (instant due to caching)
    """
    pass


class Cache:
    """
    TODO:
    A simple cache with a maximum size.
    When full, the OLDEST entry is evicted to make room for new entries.

    Methods:
        get(key)         — return value or None if not in cache
        set(key, value)  — store key-value pair; evict oldest if over max_size
        delete(key)      — remove key from cache
        clear()          — empty the cache
        size()           — return number of items in cache

    Example:
        cache = Cache(max_size=2)
        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("c", 3)  # evicts "a" (oldest)

        cache.get("a")     # None — evicted
        cache.get("b")     # 2
        cache.get("c")     # 3
    """

    def __init__(self, max_size=128):
        """
        TODO:
        Initialize with:
            self.max_size = max_size
            self._store = {}       ← key: value
            self._order = []       ← tracks insertion order (oldest first)
        """
        pass

    def get(self, key):
        """
        TODO:
        Return value for key, or None if not found.
        """
        pass

    def set(self, key, value):
        """
        TODO:
        Store key-value pair.

        If key already exists: update value (don't change order or evict).
        If key is new:
            If at max capacity: evict the OLDEST key (_order[0])
            Add new key and append to _order
        """
        pass

    def delete(self, key):
        """
        TODO:
        Remove key from cache if it exists.
        """
        pass

    def clear(self):
        """
        TODO:
        Empty the cache completely.
        """
        pass

    def size(self):
        """
        TODO:
        Return number of items currently in cache.
        """
        pass
