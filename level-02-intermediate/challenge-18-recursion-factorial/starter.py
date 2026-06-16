def factorial_recursive(n):
    """
    TODO:
    Calculate the factorial of n using RECURSION (the function calls itself).

    Factorial rules:
        0! = 1  (base case — this is mathematically defined)
        1! = 1  (base case)
        n! = n × (n-1)!  (recursive case)

    Examples:
        factorial_recursive(0)  should return 1
        factorial_recursive(1)  should return 1
        factorial_recursive(5)  should return 120   (5 × 4 × 3 × 2 × 1)
        factorial_recursive(10) should return 3628800

    Structure:
        def factorial_recursive(n):
            # Base case: when to STOP recursing
            if n <= 1:
                return 1
            # Recursive case: call yourself with a smaller number
            return n * factorial_recursive(n - 1)
    """
    pass


def factorial_iterative(n):
    """
    TODO:
    Calculate the factorial of n using a LOOP (no recursion).

    Examples:
        factorial_iterative(0)  should return 1
        factorial_iterative(1)  should return 1
        factorial_iterative(5)  should return 120
        factorial_iterative(10) should return 3628800

    Approach:
        result = 1
        for i in range(2, n + 1):  # multiply 2, 3, 4, ... up to n
            result = result * i
        return result
    """
    pass


def count_down(n):
    """
    TODO:
    Return a list counting down from n to 1 using RECURSION.

    Examples:
        count_down(5)  should return [5, 4, 3, 2, 1]
        count_down(3)  should return [3, 2, 1]
        count_down(1)  should return [1]
        count_down(0)  should return []

    Recursive approach:
        Base case: if n <= 0, return an empty list []
        Recursive case: return [n] + count_down(n - 1)

    How it works for count_down(3):
        [3] + count_down(2)
        [3] + [2] + count_down(1)
        [3] + [2] + [1] + count_down(0)
        [3] + [2] + [1] + []
        = [3, 2, 1]
    """
    pass
