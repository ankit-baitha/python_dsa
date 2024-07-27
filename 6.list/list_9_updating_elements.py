my_list = [35, 37, 45, 3, 42, 32, 2, 6, 6, 4, 9]
# my_list[-2]=435
# my_list[4]=453
# print(my_list)
print(my_list)
n = len(my_list)

for i in range(n):
    if my_list[i] % 2 == 0:
        my_list[i] = 1 + my_list[i]
    else:
        my_list[i] = my_list[i] - 1
print(my_list)
