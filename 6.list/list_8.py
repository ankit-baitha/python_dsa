# find the maximum number of list
my_list = [35, 37, 45, 3, 42, 32, 2, 6, 6, 4, 9]
n = len(my_list)
minimum = float("inf")
for i in range(0, n):
    if my_list[i] < minimum :
        minimum  = my_list[i]
print(f"minimum number of list {minimum}")
