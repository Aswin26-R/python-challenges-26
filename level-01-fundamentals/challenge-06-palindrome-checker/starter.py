def clean_string(text):
    return text.lower().replace(" ","")
    pass

def is_palindrome(text):
    cleaned = clean_string(text)
    return cleaned == cleaned[::-1]
    pass

print(clean_string("ASwin"))
print(is_palindrome("A man a plan a canal Panama"))
