# list comprehensioin is only list creation

# my_list = []
# for i in range(1, 100):
#     if i % 2 == 0:
#         my_list.append(i)
# print(my_list)

# my_list = [i for i in range(1, 11)]
# print(my_list)


my_list = [i + 3 for i in range(1, 11)]
print(my_list)


# [-1, -1, -1, -1, -1]
my_list = [-1 for i in range(1, 6)]
print(my_list)
