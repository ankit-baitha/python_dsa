# Write a function that removes duplicate characters from a given
# string.
def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result

print(remove_duplicates("programming")) 