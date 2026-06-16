def double_numbers(numbers):
    """
    TODO:
    Return a new list where each number is doubled.
    Use a list comprehension.

    Examples:
        double_numbers([1, 2, 3, 4])   should return [2, 4, 6, 8]
        double_numbers([0, -1, 5])     should return [0, -2, 10]
        double_numbers([])             should return []

    Hint: [x * 2 for x in numbers]
    """
    pass


def filter_evens(numbers):
    """
    TODO:
    Return a new list containing only the even numbers from the input list.
    Use a list comprehension with a condition.

    Examples:
        filter_evens([1, 2, 3, 4, 5, 6])  should return [2, 4, 6]
        filter_evens([1, 3, 5])            should return []  (no evens)
        filter_evens([2, 4, 6])            should return [2, 4, 6]

    Hint: [x for x in numbers if x % 2 == 0]
    """
    pass


def squares(numbers):
    """
    TODO:
    Return a new list where each number is squared (number × number).
    Use a list comprehension.

    Examples:
        squares([1, 2, 3, 4, 5])    should return [1, 4, 9, 16, 25]
        squares([-2, -1, 0, 1, 2])  should return [4, 1, 0, 1, 4]
        squares([])                  should return []

    Hint: x ** 2 squares a number (or x * x)
    """
    pass


def filter_long_words(words, min_length):
    """
    TODO:
    Return a list of words that have at least min_length characters.
    Use a list comprehension with a condition.

    Examples:
        filter_long_words(["cat", "elephant", "dog", "butterfly"], 4)
        should return ["elephant", "butterfly"]

        filter_long_words(["hi", "hello", "hey"], 3)
        should return ["hello", "hey"]

        filter_long_words(["a", "b"], 5)
        should return []

    Hint: Use len(word) >= min_length as the condition.
          [word for word in words if len(word) >= min_length]
    """
    pass


def uppercase_words(words):
    """
    TODO:
    Return a new list where each word is converted to uppercase.
    Use a list comprehension.

    Examples:
        uppercase_words(["hello", "world", "python"])
        should return ["HELLO", "WORLD", "PYTHON"]

        uppercase_words(["Mixed", "CASE", "words"])
        should return ["MIXED", "CASE", "WORDS"]

        uppercase_words([])
        should return []

    Hint: word.upper() converts a string to uppercase.
          [word.upper() for word in words]
    """
    pass
