# string is inmutable

my_sting = "ankit"
print(type(my_sting), my_sting)
print()
# by index
print("by index")
n = len(my_sting)
for i in range(0, n):
    print(my_sting[i])

print()
print("reverse strign ")
for i in range(n - 1, -1, -1):
    print(my_sting[i])

print()
print("by value")
# by value
for i in my_sting:
    print(i)
