# membership -in / not in
my_list = [3, 5, 2, 4, 4, 5, 4, 5]
print(6 in my_list)
print(10 not in my_list)


result = []
for num in my_list:
    if num not in result:
        result.append(num)
print(result)
