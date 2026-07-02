def greet(name):
    return f"Hello, {name}!"
    pass


def describe_yourself(name, role):
    return f"My name is {name} and I am a {role}."
    pass


def format_greeting(greeting, name):
    return f"{greeting}, {name}!"
    pass

print(greet("Alice"))
print(greet("Bob"))
print(describe_yourself("Aswin","Python Developer"))
print(format_greeting("Hello","Everyone"))
print(format_greeting("Good Morning","to all"))
