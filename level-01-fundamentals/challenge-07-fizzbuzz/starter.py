def fizzbuzz(n):
    for i in range(n):
        if n % 3 == 0 and n % 5 == 0:
            return 'FizzBuzz'
        elif n % 3 == 0:
            return 'Fizz'
        elif n % 5 == 0:
            return 'Buzz'
        else:
            return str(n)
        pass



def fizzbuzz_list(start, end):
    result = []
    for n in range(start,end+1):
        result.append(fizzbuzz(n))
    return result
    pass

print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))
print(fizzbuzz(11))

print(fizzbuzz_list(1,15))
