# my_char = "a"
# print(ord(my_char))

# # char to ASCII
# x = 97
# print(chr(x))


my_String = "heerjifjrklk*4u54khk"
count = 0
count1 = 0
# for ch in my_String:
#      ascii_code=ord(ch)
#      if ascii_code>=97 and ascii_code<=122:
#         count +=1
#      elif ascii_code>=65 and ascii_code<90:
#          count1 +=1

for ch in my_String:
    if "a" <= ch <= "z":
        count += 1
    if "A" <= ch <= "Z":
        count1 += 1
print(count1)
print(count)

# for ch in my_String:
#     if ord("a") <= och <= "z":
#         count += 1
#     if "A" <= ch <= "Z":
#         count1 += 1
# print(count1)
# print(count)

# my_string1 = "djwak157439&%&(*%)"

# my_string1.islower()
# print(my_string1)


def islower(user_string: str) -> bool:
    is_lower = False
    is_upper = False
    for ch in user_string:
        ascii_code = ord(ch)
        if ascii_code >= 97 and ascii_code <= 122:
            is_lower = True
        elif ascii_code >= 65 and ascii_code <= 90:
            is_upper = True
    # if is_lower == True and is_upper == False:
    #     return True
    if is_lower and not is_upper:
        return True
    return False


my_string = "djwakal57439&%$(*)%"
print(islower(my_string))
