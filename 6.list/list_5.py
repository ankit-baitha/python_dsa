# sum of all elements
my_list = [2, 4, 5, 6, 74, 5, 33, 345, 435, 3435, 345, 345]
n = len(my_list)
totat = 0
for i in range(0, n):
    totat += my_list[i]

print(" sum of all number = ", totat)

# tell me the sum of even number
total_1 = 0
for i in range(0, n):
    if my_list[i] % 2 == 0:
        total_1 += my_list[i]
print("sum of even number = ", total_1)

# tell me the sum of odd number

total_2 = 0
for num in range(0, n):
    if my_list[num] % 2 != 0:
        total_2 += my_list[num]
print("sum of all odd number = ", total_2)
