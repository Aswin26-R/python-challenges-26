import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
    pass
print(is_prime(2))


def get_primes(limit):
    primes = []
    
    for n in range(2,limit+1):
        if is_prime(n):
            primes.append(n)
    return primes
    pass
print(get_primes(10))
