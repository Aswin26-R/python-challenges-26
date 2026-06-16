def title_case(text):
    """
    TODO:
    Convert the text to Title Case: first letter of each word is uppercase,
    the rest are lowercase.

    Examples:
        title_case("hello world from python")  → "Hello World From Python"
        title_case("the QUICK brown FOX")       → "The Quick Brown Fox"
        title_case("")                           → ""

    Hint: Python strings have a built-in .title() method!
    """
    pass


def count_vowels(text):
    """
    TODO:
    Count and return the number of vowels in the text.
    Vowels are: a, e, i, o, u (both upper and lowercase count).

    Examples:
        count_vowels("Hello World")  → 3  (e, o, o)
        count_vowels("rhythm")       → 0  (no vowels)
        count_vowels("AEIOUaeiou")   → 10
        count_vowels("")             → 0

    Hint:
        count = 0
        for char in text:
            if char.lower() in "aeiou":
                count += 1
        return count
    """
    pass


def remove_duplicates(text):
    """
    TODO:
    Remove CONSECUTIVE duplicate characters.
    (Only consecutive duplicates — not all duplicates in the string.)

    Examples:
        remove_duplicates("aabbcc")  → "abc"
        remove_duplicates("hello")   → "helo"  (ll becomes l)
        remove_duplicates("aabba")   → "aba"   (the second 'a' at end is not duplicate of first)
        remove_duplicates("abc")     → "abc"   (no consecutive duplicates)
        remove_duplicates("")        → ""

    Approach:
        result = ""
        for each character in text:
            if result is empty OR character is different from last character in result:
                add character to result
        return result
    """
    pass


def truncate(text, max_length):
    """
    TODO:
    Shorten text to at most max_length characters.
    If text is longer than max_length, return the first (max_length - 3) characters + "..."
    If text fits within max_length, return it unchanged.

    Examples:
        truncate("Hello World", 8)   → "Hello..."  (5 chars + "...")
        truncate("Hello World", 5)   → "He..."     (2 chars + "...")
        truncate("Hi", 10)           → "Hi"         (fits, no truncation)
        truncate("Hello", 5)         → "Hello"      (exactly fits, no truncation)
        truncate("Hello!", 5)        → "He..."

    Hint:
        if len(text) > max_length:
            return text[:max_length - 3] + "..."
        return text
    """
    pass


def is_anagram(word1, word2):
    """
    TODO:
    Return True if word1 and word2 are anagrams of each other.
    Two words are anagrams if they contain the same letters (in any order).
    Ignore case and spaces.

    Examples:
        is_anagram("listen", "silent")          → True
        is_anagram("hello", "world")            → False
        is_anagram("Astronomer", "Moon starer") → True  (ignoring case and spaces)
        is_anagram("abc", "cba")                → True

    Approach:
        Step 1: Clean both words: lowercase and remove spaces
                clean1 = word1.lower().replace(" ", "")
        Step 2: Sort the characters of each
                sorted1 = sorted(clean1)
        Step 3: Compare — if sorted characters are equal, they're anagrams
    """
    pass
