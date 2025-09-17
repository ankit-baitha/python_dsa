

def hash_string(my_string, find_string):
    # create frequency table of size 123 (0 to 122)
    hashTable = [0] * 123  

    # count frequency of each character
    for ch in my_string:
        hashTable[ord(ch)] += 1

    # print frequency of characters in find_string
    for ch in find_string:
        print(ch, hashTable[ord(ch)])
# Example
my_string = "asdghahahed"
hash_string(my_string, "abcd")

