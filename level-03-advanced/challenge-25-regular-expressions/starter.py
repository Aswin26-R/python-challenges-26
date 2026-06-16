import re


def is_valid_email(email):
    """
    TODO:
    Return True if the email address matches a basic valid format, False otherwise.

    A valid email (for this challenge) must have:
    - One or more word characters, dots, plus signs, or hyphens BEFORE @
    - An @ symbol
    - One or more word characters or hyphens AFTER @ (domain name)
    - A dot (.)
    - One or more word characters AFTER the dot (top-level domain)

    Examples:
        is_valid_email("user@example.com")    → True
        is_valid_email("user.name@domain.org") → True
        is_valid_email("not-an-email")         → False  (no @)
        is_valid_email("user@domain")          → False  (no .com or .org)
        is_valid_email("@domain.com")          → False  (nothing before @)

    Hint: Pattern: r'^[\w.+-]+@[\w-]+\.[\w.]+$'
    Use re.match() and check if the result is not None.
    """
    pass


def extract_numbers(text):
    """
    TODO:
    Return a list of all numbers (sequences of digits) found in the text.

    Examples:
        extract_numbers("I have 3 cats and 12 dogs")  → ["3", "12"]
        extract_numbers("Worth $450 and 2 days")       → ["450", "2"]
        extract_numbers("No numbers here")             → []
        extract_numbers("Room 101 at 9pm")             → ["101", "9"]

    Hint: re.findall(r'\d+', text)
          \d matches a digit, + means one or more.
    """
    pass


def is_valid_phone(phone):
    """
    TODO:
    Return True if the phone number matches the format: +XX-XXX-XXX-XXXX
    Where X is any digit.

    Valid examples:
        "+91-987-654-3210"   → True
        "+1-800-555-1234"    → True  (wait: only 1 digit for country code)

    Actually, for this challenge, match: +{2 digits}-{3 digits}-{3 digits}-{4 digits}

    Examples:
        is_valid_phone("+91-987-654-3210")  → True
        is_valid_phone("+1-234-567-8901")   → False (only 1 country code digit)
        is_valid_phone("1234567890")        → False (no + and dashes)
        is_valid_phone("+91-98-654-3210")   → False (middle part wrong)

    Hint: Pattern: r'^\+\d{2}-\d{3}-\d{3}-\d{4}$'
    """
    pass


def replace_whitespace(text):
    """
    TODO:
    Replace consecutive whitespace (spaces and/or tabs) with a single space.

    Examples:
        replace_whitespace("hello   world")     → "hello world"
        replace_whitespace("hello\t\tworld")    → "hello world"
        replace_whitespace("a  b\t\tc  d")     → "a b c d"
        replace_whitespace("no extra spaces")   → "no extra spaces"

    Hint: re.sub(r'[ \t]+', ' ', text)
          [ \t] matches space OR tab
          + means one or more
          Replace all such sequences with a single space ' '
    """
    pass


def extract_hashtags(text):
    """
    TODO:
    Return a list of all hashtags found in the text.
    A hashtag starts with # followed by one or more word characters.

    Examples:
        extract_hashtags("I love #python and #coding is #fun")
        → ["#python", "#coding", "#fun"]

        extract_hashtags("No hashtags here")
        → []

        extract_hashtags("#hello #world")
        → ["#hello", "#world"]

    Hint: re.findall(r'#\w+', text)
          # is literal hash character
          \w+ is one or more word characters (letters, digits, underscore)
    """
    pass
