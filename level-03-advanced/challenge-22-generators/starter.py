def count_up(start, end):
    for i in range(start,end + 1):
        yield i
        pass

print(list(count_up(0,3)))

"""
    TODO:
    A generator that yields integers from start to end (inclusive).

    Examples:
        list(count_up(1, 5))   → [1, 2, 3, 4, 5]
        list(count_up(3, 3))   → [3]
        list(count_up(0, 3))   → [0, 1, 2, 3]

    Hint: Use a for loop with yield:
        for i in range(start, end + 1):
            yield i

    This is a GENERATOR FUNCTION because it uses yield.
    It does NOT return a list — it generates values one at a time.
    """


def fibonacci_generator():
    a,b = 0,1
    while True:
        yield a 
        a,b = b, a+b
    pass
fib = fibonacci_generator()
print(next(fib))
print(next(fib))
"""
    TODO:
    An INFINITE generator that yields Fibonacci numbers forever.
    Start from 0: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

    This generator never stops — callers use take() or slicing to get a limited number.

    Example:
        fib = fibonacci_generator()
        next(fib)   → 0
        next(fib)   → 1
        next(fib)   → 1
        next(fib)   → 2

    Hint:
        a, b = 0, 1
        while True:      ← infinite loop (that's OK for generators!)
            yield a      ← yield current value
            a, b = b, a + b  ← update to next fibonacci numbers
    """



def take(generator, n):
    return [next(generator) for _ in range(n)]
    pass
fib = fibonacci_generator()
print(take(fib,5))
print(take(count_up(1,100),3))
"""
    TODO:
    Return the first n values from a generator as a list.

    Examples:
        fib = fibonacci_generator()
        take(fib, 5)   → [0, 1, 1, 2, 3]
        take(fib, 3)   → [5, 8, 13]   (continues from where it left off!)

        take(count_up(1, 100), 3)  → [1, 2, 3]

    Hint:
        return [next(generator) for _ in range(n)]
    """


def squares_generator(limit):
    i =  1
    while i * i <= limit:
        yield i * i
        i  += 1
    pass
print(list(squares_generator(30)))
"""
    TODO:
    A generator that yields perfect squares (1, 4, 9, 16, ...) up to the limit (inclusive).

    Examples:
        list(squares_generator(30))   → [1, 4, 9, 16, 25]
        list(squares_generator(1))    → [1]
        list(squares_generator(0))    → []
        list(squares_generator(100))  → [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    Hint:
        i = 1
        while i * i <= limit:
            yield i * i
            i += 1
"""
