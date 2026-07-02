def is_even(number):
    return number % 2 == 0
    pass


def is_odd(number):
    return number % 2!=0
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
