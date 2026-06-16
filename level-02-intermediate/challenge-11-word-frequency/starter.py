def count_words(text):
    """
    TODO:
    Count how many times each word appears in the text.
    Return a dictionary where keys are words (lowercase) and values are their counts.
    Treat uppercase and lowercase as the same word.

    Examples:
        count_words("hello world hello")
        should return {"hello": 2, "world": 1}

        count_words("The cat sat on the mat")
        should return {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}

        count_words("")
        should return {}

    Approach:
        Step 1: Convert text to lowercase: text.lower()
        Step 2: Split into words: .split()
        Step 3: For each word, add to a dictionary:
                counts = {}
                for word in words:
                    counts[word] = counts.get(word, 0) + 1
        Step 4: Return the counts dictionary
    """
    pass


def most_common_word(text):
    """
    TODO:
    Return the word that appears most often in the text.
    If multiple words tie, return any one of them.
    Comparison is case-insensitive.

    Examples:
        most_common_word("hello world hello python hello")
        should return "hello"

        most_common_word("the cat sat on the mat")
        should return "the"

    Hint:
        Use your count_words() function to get the counts, then:
        max(counts, key=counts.get)
        This returns the key (word) with the highest value (count).
    """
    pass


def unique_words(text):
    """
    TODO:
    Return a sorted list of all unique words in the text (no duplicates).
    Words should be lowercase.

    Examples:
        unique_words("banana apple banana cherry apple")
        should return ["apple", "banana", "cherry"]

        unique_words("Hello hello HELLO")
        should return ["hello"]

        unique_words("")
        should return []

    Hint:
        Step 1: Get all words (lowercase): text.lower().split()
        Step 2: Remove duplicates using set(): set(words)
        Step 3: Sort the result: sorted(...)
    """
    pass
