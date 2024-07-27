# tuple - inmutable object
my_tuple = (2, 3, 2, 4, 24, 2, 24, 6)
print(my_tuple)
print(type(my_tuple))

n = len(my_tuple)
for i in range(n):
    print(my_tuple[i], end=" ")
print()
for i in my_tuple:
    print(i, end=" ")

print(my_tuple.count(2))


a = 34, 5, 53, 25
print(a)
print(type(a))
