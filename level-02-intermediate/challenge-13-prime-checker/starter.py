import math


def is_prime(n):
    """
    TODO:
    Return True if n is a prime number, False otherwise.

    A prime number is a number greater than 1 with no divisors except 1 and itself.

    Examples:
        is_prime(2)   should return True   (2 is the smallest prime)
        is_prime(3)   should return True
        is_prime(4)   should return False  (4 = 2 × 2)
        is_prime(17)  should return True
        is_prime(1)   should return False  (1 is NOT prime by definition)
        is_prime(0)   should return False
        is_prime(-5)  should return False

    Algorithm:
        Step 1: If n < 2, return False immediately

        Step 2: Check if n has any divisors from 2 up to sqrt(n):
                for i in range(2, int(math.sqrt(n)) + 1):
                    if n % i == 0:
                        return False  # found a divisor, not prime

        Step 3: If no divisor found, return True

    Why sqrt(n)? If n has a factor larger than sqrt(n),
    it must also have a factor smaller than sqrt(n).
    So we only need to check up to sqrt(n).
    """
    pass


def get_primes(limit):
    """
    TODO:
    Return a list of all prime numbers from 2 up to and including limit.

    Examples:
        get_primes(10)  should return [2, 3, 5, 7]
        get_primes(20)  should return [2, 3, 5, 7, 11, 13, 17, 19]
        get_primes(2)   should return [2]
        get_primes(1)   should return []
        get_primes(0)   should return []

    Hint: Use a loop and call your is_prime() function:
        primes = []
        for n in range(2, limit + 1):
            if is_prime(n):
                primes.append(n)
        return primes
    """
    pass
