def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)
    pass
print(factorial_recursive(5))

def factorial_iterative(n):
    result = 1
    for i in range(2,n+1):
        result = result * i
    return result
    pass
print(factorial_iterative(10))

def count_down(n):
    if n <=0:
        return []
    return [n] + count_down(n-1)
    pass
print(count_down(0))