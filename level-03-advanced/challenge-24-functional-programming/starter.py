from functools import reduce


def apply_to_all(func, items):
    """
    TODO:
    Apply func to every item in the items list and return the results as a new list.
    Use map() internally.

    Examples:
        apply_to_all(lambda x: x * 2, [1, 2, 3, 4])  → [2, 4, 6, 8]
        apply_to_all(str, [1, 2, 3])                   → ["1", "2", "3"]
        apply_to_all(lambda x: x ** 2, [1, 2, 3])     → [1, 4, 9]

    Hint: list(map(func, items))
    """
    pass


def keep_if(func, items):
    """
    TODO:
    Return a new list containing only items for which func returns True.
    Use filter() internally.

    Examples:
        keep_if(lambda x: x > 3, [1, 2, 3, 4, 5, 6])       → [4, 5, 6]
        keep_if(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])  → [2, 4, 6]
        keep_if(lambda s: len(s) > 3, ["hi", "hello", "hey"]) → ["hello"]

    Hint: list(filter(func, items))
    """
    pass


def reduce_list(func, items, initial):
    """
    TODO:
    Combine all items in the list into a single value using func.
    Start with 'initial' as the accumulator.

    How reduce works:
        result = initial
        for each item in items:
            result = func(result, item)
        return result

    Examples:
        reduce_list(lambda acc, x: acc + x, [1, 2, 3, 4, 5], 0)  → 15  (sum)
        reduce_list(lambda acc, x: acc * x, [1, 2, 3, 4], 1)      → 24  (product)
        reduce_list(lambda acc, x: acc + [x*2], [1,2,3], [])       → [2, 4, 6]

    Hint: from functools import reduce  (already imported at top)
          reduce(func, items, initial)
    """
    pass


def pipeline(value, *funcs):
    """
    TODO:
    Apply each function in funcs to the value in order, passing each result to the next.

    Examples:
        pipeline(5, lambda x: x * 2, lambda x: x + 1, lambda x: x ** 2)
        → 5 → (×2) → 10 → (+1) → 11 → (²) → 121

        pipeline("hello", str.upper, lambda s: s + "!")
        → "hello" → "HELLO" → "HELLO!"

    Approach:
        result = value
        for func in funcs:
            result = func(result)
        return result
    """
    pass


def compose(f, g):
    """
    TODO:
    Return a new function that first applies g, then applies f to the result.
    This is mathematical function composition: (f ∘ g)(x) = f(g(x))

    Examples:
        add_one = lambda x: x + 1
        double = lambda x: x * 2

        add_then_double = compose(double, add_one)
        add_then_double(5)  → double(add_one(5)) = double(6) = 12

        double_then_add = compose(add_one, double)
        double_then_add(5)  → add_one(double(5)) = add_one(10) = 11

    Hint: return lambda x: f(g(x))
    """
    pass
