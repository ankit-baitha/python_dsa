# my_string = "aeghuernir"
# total = 0
# for ch in my_string:
#     if ch in "aeiouAEIOU":
#         total += 1
# print(total)

# # question

# def longest_word(s: str) -> str:
#     longest = ""
#     current = ""
#     for char in s:
#         if char == " ":
#             if len(current) > len(longest):
#                 longest = current
#             current = ""
#         else:
#             current += char
#     if len(current) > len(longest):
#         longest = current
#     return longest

# my_string = "python is a very easy coding language to learn"
# print(longest_word(my_string))


# my_sting = "python is a good language"
# ans = list(my_sting)
# print(ans)


# spliting
# by default whitespace _. space, enter ,tab....
# my_string = "python is a good language"
# ans = my_string.split()
# print(ans)

# my_string = "python is a good language"
# ans = my_string.split("g")
# print(ans)

# my_string = "python is a good language"
# print(len(my_string.split()))


# SPlit -> String to List
# Joining -> List to String

# a n i r u d h
# my_list = ["a", "n", "i", "r", "u", "d", "h"]

# # result = "".join(ch for ch in my_list)
# result = "-".join(ch + "5" for ch in my_list)
# print(result)
# my_list = ["a", 4, 5, 6, 7, 8, 7, "Anirudh", "x", "y", "z"]
# print("".join(str(ch) for ch in my_list))


# my_string = "python is a good language"
# word = my_string.split()
# print(word)
# # reverse
# word = word[::-1]
# print(word)

# ans = " ".join(i for i in word)
# print(ans)


# my_string = "python is a good language"
# # nohtyp si a doog egaugnal
# words = my_string.split()
# print(words)
# print("-".join(word[::-1] for word in words))
# result = ""
# for word in words:
#     result = result + word[::-1]
#     result += "-"
# print(result)
# print(result[:-1])


# my_string = "python is a good language"
# # Output 👇
# # egaugnal doog a si nohtyp
# words = my_string.split()
# # words.reverse()
# print(" ".join(word[::-1] for word in words[::-1]))


# my_list = [4, 5, 3, 2, 7, 8, 6, 8, 9, 3]
# print(my_list)
# print(id(my_list))
# my_list.sort()  # In place sorting
# print(my_list)
# print(id(my_list))
# print(sorted(my_list))
# print(my_list)

my_list = [4, 5, 3, 2, 7, 8, 6, 8, 9, 3]
# print("-".join(str(num) for num in my_list.sort()))
print("-".join(str(num) for num in sorted(my_list)))
print(my_list)
