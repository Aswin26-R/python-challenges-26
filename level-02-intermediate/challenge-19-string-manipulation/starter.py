def title_case(text):
    return text.title()
    pass
print(title_case("hello world from python"))

def count_vowels(text):
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count 
    pass
print(count_vowels("Hello world"))

def remove_duplicates(text):
    result = ""
    for char in text:
        if result == "" or char != result[-1]:
            result += char
    return result
    pass
print(remove_duplicates("aabbcc"))

def truncate(text, max_length):
    if len(text) > max_length:
        return text[:max_length - 3] + "..."
    return text
    pass
print(truncate("Hello World", 5))

def is_anagram(word1, word2):
    clean1 = word1.lower().replace(" ","")
    clean2 = word2.lower().replace(" ","")
    sorted1 = sorted(clean1)
    sorted2 = sorted(clean2)
    if sorted1 == sorted2:
        return True
    else:
        return False
    pass
print(is_anagram("listen","silent"))