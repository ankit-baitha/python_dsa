my_list = [4, 5, 6, 4, 4, 3, 2, 3, 3, 10, 4, 8, 9, 9, 10]
"""
{
    4:6,
    5:1,
    6:1,
    10:1,
}
"""

my_dict = {}
for num in my_list:
    if num in my_dict:
        my_dict[num] = my_dict[num] + 1
    else:
        my_dict[num] = 1
print(my_dict)

# method 2

my_list = [4, 5, 6, 4, 4, 3, 2, 3, 3, 10, 4, 8, 9, 9, 10]
"""
{
    
}
"""
my_dict = {}
for num in my_list:
    my_dict[num] = my_dict.get(num, 0) + 1
print(my_dict)
