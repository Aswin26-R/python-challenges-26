def fibonacci(n):
    """
    TODO:
    Return the nth Fibonacci number (0-indexed).

    The Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    - fibonacci(0) = 0   (index 0 → value 0)
    - fibonacci(1) = 1   (index 1 → value 1)
    - fibonacci(2) = 1   (0 + 1 = 1)
    - fibonacci(3) = 2   (1 + 1 = 2)
    - fibonacci(7) = 13

    Approach:
        Handle base cases first:
            if n == 0: return 0
            if n == 1: return 1

        Then use a loop:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return b

    The trick: a, b = b, a + b
        This is Python's way to swap and update both variables at once.
        Right side is evaluated first, THEN assigned.
    """
    pass


def fibonacci_sequence(count):
    """
    TODO:
    Return a list containing the first 'count' Fibonacci numbers.

    Examples:
        fibonacci_sequence(5)   should return [0, 1, 1, 2, 3]
        fibonacci_sequence(10)  should return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        fibonacci_sequence(1)   should return [0]
        fibonacci_sequence(0)   should return []

    Approach:
        Handle edge cases: if count is 0, return []
        Start with a list: sequence = [0, 1]
        Then keep adding: next = sequence[-1] + sequence[-2]
        Stop when you have 'count' numbers.

        Or use a loop with a, b = 0, 1 and append each value.
    """
    pass
