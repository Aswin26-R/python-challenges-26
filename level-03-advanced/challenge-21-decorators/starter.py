import functools
import time
"""
    TODO:
    A decorator that measures and prints how long the wrapped function takes to run.

    After the function completes, print a message in this exact format:
    "{function_name} took {elapsed:.2f} seconds"

    Example:
        @timer
        def slow_function():
            time.sleep(0.1)
            return "done"

        result = slow_function()
        # Prints: "slow_function took 0.10 seconds"
        # result == "done"

    Structure:
        def timer(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                elapsed = end - start
                print(f"{func.__name__} took {elapsed:.2f} seconds")
                return result
            return wrapper
"""
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f"{func.__name__} took {elapsed:.2f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "done"
result =  slow_function
print(slow_function())



"""
    TODO:
    A decorator that logs (prints) information about function calls.

    Before calling the function, print:
    "Calling {function_name} with args={args} kwargs={kwargs}"

    After the function returns, print:
    "{function_name} returned {result}"

    Then return the result.

    Example:
        @logger
        def add(a, b):
            return a + b

        result = add(3, 4)
        # Prints: "Calling add with args=(3, 4) kwargs={}"
        # Prints: "add returned 7"
        # result == 7
"""
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
        # TODO: Print the "Calling..." message, call func, print the "returned" message, return result
        pass
    return wrapper
@logger
def add(a,b):
    return a + b

result = add(3,4) 
print(result)




"""
    TODO:
    A decorator that validates all positional arguments are positive numbers (> 0).
    If any argument is 0 or negative, raise ValueError("All arguments must be positive").
    If all arguments are positive, call the function normally and return the result.

    Example:
        @validate_positive
        def multiply(a, b):
            return a * b

        multiply(3, 4)    → returns 12
        multiply(-1, 4)   → raises ValueError("All arguments must be positive")
        multiply(0, 5)    → raises ValueError("All arguments must be positive")

    Hint:
        for arg in args:
            if arg <= 0:
                raise ValueError("All arguments must be positive")
        return func(*args, **kwargs)
"""
def validate_positive(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <= 0:
                raise ValueError("All arguments must be positive")
        return func(*args,**kwargs)
        # TODO: Check each argument, raise ValueError if any is not positive, then call func
        pass
    return wrapper

@validate_positive
def multiply(a,b):
    return a*b

print(multiply(3,4))
