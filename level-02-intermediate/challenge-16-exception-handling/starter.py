def safe_divide(a, b):
    """
    TODO:
    Divide a by b and return the result.
    If b is zero, return None instead of raising an exception.

    Examples:
        safe_divide(10, 2)   should return 5.0
        safe_divide(10, 0)   should return None  (not an error, just None)
        safe_divide(7, 2)    should return 3.5
        safe_divide(0, 5)    should return 0.0

    Hint:
        try:
            return a / b
        except ZeroDivisionError:
            return None
    """
    pass


def safe_int_convert(value):
    """
    TODO:
    Convert the value to an integer and return it.
    If the conversion fails (e.g., value is a non-numeric string), return None.

    Examples:
        safe_int_convert("42")     should return 42
        safe_int_convert("hello")  should return None
        safe_int_convert(3.7)      should return 3   (int() truncates)
        safe_int_convert("3")      should return 3
        safe_int_convert(None)     should return None

    Hint:
        try:
            return int(value)
        except (ValueError, TypeError):
            return None
    """
    pass


def get_list_item(lst, index):
    """
    TODO:
    Return the item at the given index in the list.
    If the index is out of range, return None instead of raising an exception.

    Examples:
        get_list_item([10, 20, 30], 1)   should return 20
        get_list_item([10, 20, 30], 99)  should return None
        get_list_item([10, 20, 30], -1)  should return 30  (negative index works)
        get_list_item([], 0)             should return None

    Hint:
        try:
            return lst[index]
        except IndexError:
            return None
    """
    pass


def validate_age(age):
    """
    TODO:
    Validate that the age is a reasonable number (0 to 150, inclusive).
    If valid, return True.
    If invalid, RAISE a ValueError with the message: "Age must be between 0 and 150"

    Examples:
        validate_age(25)   should return True
        validate_age(0)    should return True
        validate_age(150)  should return True
        validate_age(-1)   should raise ValueError("Age must be between 0 and 150")
        validate_age(200)  should raise ValueError("Age must be between 0 and 150")

    Note: This function RAISES an error — it does NOT use try/except.
    Use if/raise:
        if age < 0 or age > 150:
            raise ValueError("Age must be between 0 and 150")
        return True
    """
    pass
