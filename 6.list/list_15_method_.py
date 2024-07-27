# list methods(function)
my_list: list = [3, 4, 53, 4, 3, 5]
# my_list.append([3,4,4,4])
# print(my_list)


# extend()
my_list.extend([34, 35, 5, 2, 5])
print(my_list)

# count()
countingOfNumber = my_list.count(4)
print(my_list)
print(countingOfNumber)


# index by value
x = my_list.index(5)
print(x)

my_list.sort()
# sort
print("sorted by list method : ", my_list)
