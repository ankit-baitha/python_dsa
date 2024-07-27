# list method (function)
# insert

my_list = [34.4, 4, 3, 43, 43, 3, 54]
my_list.insert(4, 200)  # fist is index number and second is value
print(my_list)
# not index number then  fill the last index
my_list.insert(50, 1000)
print(my_list)


my_list.insert(-1, 400)  # all elements are shift right side
print(my_list)


# pop method # by default value is -1
x = my_list.pop()
print(x)
print(my_list)
z = my_list.pop(0)
print(z)
print(my_list)


# del

my_list_1 = [3, 5, 3, 56, 3, 54, 53, 34, 75]
print(" my list ", my_list_1)
del my_list_1[2]  # delete by index
print(" deleted list", my_list_1)

# remove
print(my_list_1)
my_list_1.remove(56)  # delete by value

# clear
my_list.clear()
print(my_list)
