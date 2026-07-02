def is_even(number):
    return number % 2 == 0
    pass


def is_odd(number):
    return number % 2!=0
    """
    TODO:
    Return True if the number is odd, False if the number is even.

    Examples:
        is_odd(3)   should return True
        is_odd(-4)  should return False
        is_odd(0)   should return False
        is_odd(7)   should return True

    Hint: A number is odd when it is NOT even.
          You can use your is_even() function here, or check number % 2 != 0.
    """
    pass


def classify_number(number):
    if number % 2==0:
        return "even"
    else:
        return "odd"
    pass

print(is_even(2))
print(is_odd(5))
print(classify_number(-5))
