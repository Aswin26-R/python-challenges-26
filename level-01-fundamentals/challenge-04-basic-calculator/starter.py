def add(a, b):
    return (a+b)
    pass


def subtract(a, b):
    return (a-b)
    pass


def multiply(a, b):
    return a*b
    pass


def divide(a, b):
    if b == 0:
        return None
    else:
        return a/b
    pass


def calculate(a, operator, b):
    if operator == "+" :
        return add(a,b)
    elif operator == '-':
        return subtract(a,b)
    elif operator == '*':
        return multiply(a,b)
    elif operator == '/':
        return divide(a,b)
    else :
        return None
    pass


print(add(1,2))
print(subtract(5,-9))
print(multiply(3,5))
print(divide(30,0))
print(calculate(10,"@",10))
