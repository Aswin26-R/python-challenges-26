def add(a, b):
    """
    TODO:
    Return the sum of a and b.

    Examples:
        add(3, 4)    should return 7
        add(-1, 1)   should return 0
        add(0, 0)    should return 0
        add(1.5, 2)  should return 3.5
    """
    pass


def subtract(a, b):
    """
    TODO:
    Return a minus b.

    Examples:
        subtract(10, 3)  should return 7
        subtract(0, 5)   should return -5
        subtract(5, 5)   should return 0
    """
    pass


def multiply(a, b):
    """
    TODO:
    Return a multiplied by b.

    Examples:
        multiply(4, 5)   should return 20
        multiply(-2, 3)  should return -6
        multiply(0, 99)  should return 0
    """
    pass


def divide(a, b):
    """
    TODO:
    Return a divided by b.
    If b is zero, return None (you cannot divide by zero).

    Examples:
        divide(10, 2)  should return 5.0
        divide(7, 2)   should return 3.5
        divide(10, 0)  should return None  ← important edge case!
        divide(0, 5)   should return 0.0

    Hint: Check if b == 0 before dividing. Use:
        if b == 0:
            return None
    """
    pass


def calculate(a, operator, b):
    """
    TODO:
    Perform the arithmetic operation specified by the operator string.

    Parameters:
        a        — the first number
        operator — one of: "+", "-", "*", "/"
        b        — the second number

    Return the result of the operation.
    If the operator is unknown or division by zero occurs, return None.

    Examples:
        calculate(3, "+", 4)   should return 7
        calculate(10, "-", 3)  should return 7
        calculate(4, "*", 5)   should return 20
        calculate(10, "/", 2)  should return 5.0
        calculate(10, "/", 0)  should return None
        calculate(5, "@", 2)   should return None  (unknown operator)

    Hint: Use if/elif to check which operator was given:
        if operator == "+":
            return add(a, b)
        elif operator == "-":
            ...
    """
    pass
