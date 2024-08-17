"""  """# Q1. write a function that takes string and return it reversed.
def reverse(n: str) -> str:
    reversestr = ""
    for i in range(len(n) - 1, -1, -1):
        reversestr += n[i]
    return reversestr


# n=input("enter words ")
# print(reverse(n))


# Q2. write a function that takes a string and returns it in uppercase.
def reverse(n: str) -> str:
    uppercase = ""
    for i in n:
        ascii_code = ord(i)
        if ascii_code >= 65 and ascii_code <= 90:
            uppercase += i
    return uppercase


# n=input("enter words ")
# print(reverse(n))


# Q3. write a function that removes all vowels (a,e,i,o,u) from a given string.
def removes(my_string: str):
    for ch in range(len(my_string)):
        if my_string[ch] in "aeiouAEIOU":
            vowels = my_string[ch]
        else:
            print(my_string[ch], end="")


# removes("DRCDIieaaimuU")


# Q4. write a function that counts the number of words in given string (string may only contain alphabetes and spaces)
def Count(my_string: str) -> None:
    total = 0
    for ch in my_string:
        ascii_code = ord(ch)
        if (
            ascii_code >= 65
            and ascii_code <= 90
            or ascii_code >= 97
            and ascii_code <= 122
            or ascii_code == 32
        ):
            total += 1
    return total


# my_string = input("enter cheraters ")
# print(Count(my_string))


# Q5. write a function that finds and returns that longest word in a given string.
def longest(my_string: str) -> str:
    longest = ""
    current = ""
    for ch in my_string:
        if ch == " ":
            if len(current) > len(longest):
                longest = current
            current = " "
        else:
            current += ch
    if len(current) > len(longest):
        longest = current
    return longest


# print(longest("python is programming language "))


# Q8. Write a function that removes all non-alphabetic characters from a given string.


def non_alphabetic(my_string: str):
    alphabetic = ""
    for ch in my_string:
        ascii_code = ord(ch)
        if (
            ascii_code >= 65
            and ascii_code <= 90
            or ascii_code >= 97
            and ascii_code <= 122
        ):
            alphabetic += ch
    print(alphabetic)


# my_string = input("enter the sentance = ")
# non_alphabetic(my_string)


# Q9. Write a function that counts the number of digits in a given string.
def count_digits(my_string: str):
    digit = 0
    for ch in my_string:
        ascii_code = ord(ch)
        if ascii_code >= 48 and ascii_code < 57:
            digit += 1
    print(digit)
# my_string = input("enter the sentance = ")
# count_digits(my_string)
# Q10. Write a function that removes duplicate characters from a given string.
def duplicate(my_string:str):
    d=dict()
    a=''
    # for i in my_string:
    #     if i not in a:
    #         a=a+i
    # return a

if __name__=="__main__":
    print(duplicate("mmmdemdeh"))
        
# Q11. Write a function that checks if a given string contains only alphanumeric characters.
# Q12. Write a function that replaces all spaces in a given string with hyphens (-).
