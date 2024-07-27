# remove even number in the my list
my_list = [3, 7, 6, 6, 7, 3, 2, 7, 3, 4, 6, 3, 3, 2]

# n = len(my_list)
# print(n)
# for i in range(0, n):
#     if my_list[i] % 2 == 0:
#         my_list.pop(i)
# print(my_list)
# index error

my_list = [3, 7, 6, 6, 7, 3, 2, 7, 3, 4, 6, 3, 3, 2]
result = []
n = len(my_list)
for i in range(0, n):
    if my_list[i] % 2 != 0:
        result.append(my_list[i])

print(result)
