my_string = "python is a good language"
word = my_string.split()
print(word)
# reverse
word = word[::-1]
print(word)
ans = " ".join(i for i in word)
print(ans)
