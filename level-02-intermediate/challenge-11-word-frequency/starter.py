def count_words(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        counts[word]= counts.get(word,0) + 1
    return counts 
    pass
print(count_words("hello world hello"))   

def most_common_word(text):
    counts = count_words(text)
    if not counts:
        return None
    return max(counts, key = counts.get)
    pass
print(most_common_word("the cat sat on the mat"))


def unique_words(text):
    words = text.lower().split()
    return sorted(set(words))
    pass
print(unique_words("banana apple banana cherry apple"))
