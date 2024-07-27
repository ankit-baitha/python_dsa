my_string = "dhaw43789HGDSAK&*(#$  HDK486/*-+daw)"
aplhabets = 0
digit = 0
space = 0
symbols = 0

for ch in my_string:
    ascii_code = ord(ch)
    if ascii_code >= 97 and ascii_code <= 122 or ascii_code >= 65 and ascii_code <= 90:
        aplhabets += 1
    elif ascii_code >= 48 and ascii_code <= 57:
        digit += 1

    elif ascii_code == 32:
        space += 1
    else:
        symbols += 1

print("alphabets", aplhabets)
print("digit", digit)
print("space", space)
print("symbols", symbols)
