my_string = "dfghreetSDFGHjkHJ%$^&JH6RFghchgjh88yug"
count = 0
count_1 = 0
# for ch in my_string:
#     ascii_code = ord(ch)
#     if ascii_code >= 97 and ascii_code <= 122:
#         count += 1
#     elif ascii_code >= 65 and ascii_code <= 90:
#         count_1 += 1
# print(f"Total lowercase letter = {count} ")
# print(f"Total uppercase letter = {count_1} ")


# method 2
for ch in my_string:
    if "a" <= ch <= "z":
        count += 1
    elif "A" <= ch <= "Z":
        count_1 += 1
print(f"Total lowercase letter = {count} ")
print(f"Total uppercase letter = {count_1} ")
