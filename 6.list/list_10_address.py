my_list = [3, 3, 5, 4, 5, 32, 6, 5, 2, 43, 5]
print(id(my_list))
print(my_list)

my_list[3] = 10000
print(id(my_list))
print(my_list)
