def fibonacci(n):
    a,b = 0,1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for _ in range(n - 1):
            a,b = b, a+b
        return b
    pass
print(fibonacci(7))

def fibonacci_sequence(count):
    if count == 0:
        return []
    
    sequence = []
    a,b = 0,1
    
    for _ in range(count):
        sequence.append(a)
        a,b = b,a+b
    return sequence 

    pass
print(fibonacci_sequence(10))
