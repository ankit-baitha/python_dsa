# Write a function that takes a string and returns it in uppercase.

def to_uppercase(text):
    return text.upper()


result = to_uppercase("hello world")
print(result)  

def to_uppercase_(text):
    result=""
    for ch in text:
        ascii_code=ord(ch)
        if ascii_code>=97 and ascii_code<=122:
            ascii_code-=32
            result = result + chr(ascii_code)
        else:
            result= result + ch
    return result
text="hello World"
print(to_uppercase_(text))