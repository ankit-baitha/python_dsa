# find the maximum number of list
my_list = [35, 37, 45, 3, 42, 32, 2, 6, 6, 4, 9]
n = len(my_list)
maxi = 0
for i in range(0, n):
    if my_list[i] > maxi:
        maxi = my_list[i]
print(maxi)


"""
Also check the solution below will be used in dsa
""" ""
maximum = float("-inf")
for i in range(n):
    maximum = max(maximum, my_list[i])
print("maximum number of list = ", maximum)
