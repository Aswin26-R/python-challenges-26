def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None
    pass
print(safe_divide(10, 2))

def safe_int_convert(value):
    try:
        return int(value)
    except(ValueError,TypeError):
        return None
    pass
print(safe_int_convert("hello"))

def get_list_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None
    pass
print(get_list_item([10,20,30],-1))

def validate_age(age):
    if age < 0 or age > 150:
        raise ValueError("Age must be between 0 and 150")
    return True
    pass
print(validate_age(100))
