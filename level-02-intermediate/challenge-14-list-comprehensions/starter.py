def double_numbers(numbers):
    return [x * 2 for x in numbers]
    pass
print(double_numbers([1,2,3,4]))

def filter_evens(numbers):
    return [x for x in numbers if x % 2 == 0]
    pass
print(filter_evens([1,3,5]))

def squares(numbers):
    return [x ** 2 for x in numbers]
    pass
print(squares([1,2,3,4,5]))

def filter_long_words(words, min_length):
    result = []
    for word in words:
        if len(word) >= min_length:
            result.append(word)
    return result
    pass
print(filter_long_words(["hi",'hello','hey'],3))

def uppercase_words(words):
    return [word.upper() for word in words] 
    pass
print(uppercase_words(["hello",'hi','world','python']))