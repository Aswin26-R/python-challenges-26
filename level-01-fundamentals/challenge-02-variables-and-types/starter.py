def get_type_name(value):
    return type(value).__name__
    pass


def is_integer(value):
    return isinstance(value, int) and not isinstance(value, bool)
    pass


def is_string(value):
    return isinstance(value, str)
    pass


def convert_to_int(value):
    return int(value)
    pass


def convert_to_string(value):
    return str(value)
    pass


def add_numbers(a, b):
    return (a+b)
    pass

print(get_type_name(True))
print(is_integer('Aswin'))
print(is_string("Aswin"))
print(convert_to_int(3))
print(convert_to_string("Hi"))
print(add_numbers(22,88))
