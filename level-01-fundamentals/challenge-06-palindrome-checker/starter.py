def clean_string(text):
    """
    TODO:
    Return the text converted to lowercase with all spaces removed.

    This is a "helper function" — it prepares text for palindrome checking.

    Examples:
        clean_string("Hello World")  should return "helloworld"
        clean_string("Race Car")     should return "racecar"
        clean_string("MADAM")        should return "madam"
        clean_string("hello")        should return "hello"
        clean_string("")             should return ""

    Hint: Chain two string methods:
        Step 1: text.lower()          → converts to lowercase
        Step 2: result.replace(" ", "") → removes spaces
    """
    pass


def is_palindrome(text):
    """
    TODO:
    Return True if the text is a palindrome, False otherwise.

    Rules:
    - Ignore case ("Madam" and "madam" are the same)
    - Ignore spaces ("race car" and "racecar" are the same)
    - An empty string is a palindrome
    - A single character is always a palindrome

    Examples:
        is_palindrome("racecar")                        should return True
        is_palindrome("hello")                          should return False
        is_palindrome("Madam")                          should return True
        is_palindrome("A man a plan a canal Panama")    should return True
        is_palindrome("")                               should return True
        is_palindrome("a")                              should return True

    Approach:
        Step 1: Clean the text using your clean_string() function
        Step 2: Compare the cleaned text to its reverse
                cleaned == cleaned[::-1]
    """
    pass
