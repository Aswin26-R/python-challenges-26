def reverse_string(text):
    """
    TODO:
    Return the string with all characters in reverse order.

    Examples:
        reverse_string("hello")  should return "olleh"
        reverse_string("Python") should return "nohtyP"
        reverse_string("")       should return ""   (empty string)
        reverse_string("a")      should return "a"  (single character)
        reverse_string("12345")  should return "54321"

    Hint: Python strings support slicing with a step:
          text[::-1]  reads the string backwards (step = -1)

    This works because:
        text[start:stop:step]
        text[::-1] means: start at end, go to beginning, step -1 (backwards)
    """
    pass


def reverse_words(sentence):
    """
    TODO:
    Return the sentence with the ORDER OF WORDS reversed.
    (Not the characters — reverse the words themselves.)

    Examples:
        reverse_words("hello world")     should return "world hello"
        reverse_words("I love Python")   should return "Python love I"
        reverse_words("one")             should return "one"
        reverse_words("a b c")           should return "c b a"

    Hint: Break this into three steps:
        Step 1: Split the sentence into a list of words
                words = sentence.split()  → ["hello", "world"]

        Step 2: Reverse the list
                words.reverse()  or  words[::-1]  → ["world", "hello"]

        Step 3: Join the words back with a space between them
                result = " ".join(words)  → "world hello"
    """
    pass
