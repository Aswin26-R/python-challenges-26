def reverse_string(text):
    return text[::-1]
    pass

def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)
    pass

print(reverse_string("hello"))
print(reverse_words("hello world"))