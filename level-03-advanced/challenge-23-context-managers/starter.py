import time
from contextlib import contextmanager

class Timer:
    
    def __init__(self):
        self.elapsed = 0
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self
        # TODO: Record start time and return self
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        self.elapsed = end - self.start
        return False
        # TODO: Calculate elapsed time and store in self.elapsed
        # Return False to not suppress exceptions
        pass
    
with Timer() as t:
    time.sleep(2)
print(t.elapsed)

"""
    TODO:
    A context manager that measures how long code inside the 'with' block takes.

    After the block exits, self.elapsed should contain the elapsed time in seconds.

    Usage:
        with Timer() as t:
            do_something()
        print(t.elapsed)   # time in seconds

    You need to implement __enter__ and __exit__:

    __enter__:
        - Record the start time: self.start = time.time()
        - Return self (so 'as t' gives you the Timer object)

    __exit__(self, exc_type, exc_val, exc_tb):
        - Record the end time
        - Calculate: self.elapsed = end - self.start
        - Return False (don't suppress exceptions)
    """


@contextmanager
def managed_list():
    items = []
    yield items
    
    pass
with managed_list() as items:
    items.append(1)
    items.append(2)
print(items)
"""
    TODO:
    A generator-based context manager that creates and yields an empty list.
    The caller can append items to it inside the 'with' block.

    Usage:
        with managed_list() as items:
            items.append(1)
            items.append(2)
        # items == [1, 2]

    Structure:
        @contextmanager
        def managed_list():
            items = []       # create the list
            yield items      # give it to the caller
            # after yield, items contains what the caller added
"""
    


class suppress_errors:
    
    def __init__(self, *exception_types):
        self.exception_types = exception_types
        # TODO: Store the exception types
        pass

    def __enter__(self):
        return self
        # TODO: Return self
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type,self.exception_types):
            return True
        return False
    
        # TODO: Return True if exc_type is one of the suppressed types, False otherwise
        pass
with suppress_errors(ValueError):
    int("not a number")
with suppress_errors(ValueError, TypeError):
    raise ValueError("ignored")
with suppress_errors(ValueError):
    raise TypeError("not suppressed") 
    
print("program continues......")


"""
    TODO:
    A context manager that suppresses (ignores) specified exception types.
    If an exception of one of the specified types occurs, it is silently caught.
    Other exception types are NOT suppressed.

    Usage:
        with suppress_errors(ValueError):
            int("not_a_number")   # suppressed — code continues after the block

        with suppress_errors(ValueError, TypeError):
            raise ValueError("ignored")  # suppressed

        with suppress_errors(ValueError):
            raise TypeError("not suppressed")  # propagates normally

    Implementation:
        def __init__(self, *exception_types):
            self.exception_types = exception_types

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is not None and issubclass(exc_type, self.exception_types):
                return True   # True = suppress the exception
            return False      # False = let the exception propagate
    """
