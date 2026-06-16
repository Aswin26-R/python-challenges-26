def fizzbuzz(n):
    """
    TODO:
    Return the correct FizzBuzz string for the given number n.

    Rules:
    - If n is divisible by both 3 and 5: return "FizzBuzz"
    - If n is divisible by 3 only:       return "Fizz"
    - If n is divisible by 5 only:       return "Buzz"
    - Otherwise:                          return the number as a string

    Examples:
        fizzbuzz(1)   should return "1"
        fizzbuzz(2)   should return "2"
        fizzbuzz(3)   should return "Fizz"
        fizzbuzz(4)   should return "4"
        fizzbuzz(5)   should return "Buzz"
        fizzbuzz(6)   should return "Fizz"
        fizzbuzz(10)  should return "Buzz"
        fizzbuzz(15)  should return "FizzBuzz"

    IMPORTANT: Check for both 3 AND 5 (FizzBuzz) FIRST.
               If you check 3 first, the number 15 would return "Fizz" by mistake.

    Hint: Use if/elif/else. The number as a string is: str(n)
    """
    pass


def fizzbuzz_list(start, end):
    """
    TODO:
    Return a list of FizzBuzz results for all numbers from start to end, inclusive.

    Examples:
        fizzbuzz_list(1, 5)    should return ["1", "2", "Fizz", "4", "Buzz"]
        fizzbuzz_list(13, 16)  should return ["13", "14", "FizzBuzz", "16"]
        fizzbuzz_list(1, 1)    should return ["1"]
        fizzbuzz_list(15, 15)  should return ["FizzBuzz"]

    Hint:
        Step 1: Create an empty list: result = []
        Step 2: Use a for loop from start to end (inclusive):
                for n in range(start, end + 1):
        Step 3: For each n, call fizzbuzz(n) and append the result:
                result.append(fizzbuzz(n))
        Step 4: Return the result list
    """
    pass
