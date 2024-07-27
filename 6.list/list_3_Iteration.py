my_list = [2, 4, 5, 6, 74, 5, 33, 345, 435, 3435, 345, 345]

# Iteration by index
n = len(my_list)
for i in range(0, n):
    print(my_list[i], end=" ")
print()
for i in range(n - 1, -1, -1):
    print(my_list[i], end=" ")
