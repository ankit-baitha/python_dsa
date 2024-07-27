# deep shallow

a = [1, 2, 3, 4, 5, 5, 56, 7]

b = a  # it is address copy
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"a= {a}")
print(f"b= {b}")

b[0] = 1000
print(f"a= {a}")
print(f"b= {b}")


print()
c = [2, 3, 4, 5, 56, 6, 6, 8]
d = c.copy()  # shallow copy  address change
print(f"id(c) = {id(c)}")
print(f"id(d) = {id(d)}")
print(f"a= {c}")
print(f"b= {d}")

d[0] = 1000
print(f"a= {c}")
print(f"b= {d}")

print()
# deep copy
from copy import deepcopy

i = [2, 4, 44, 4, [234, 343, 43], 32]
j = deepcopy(i)

print(f"id(i) {id(i)}")
print(f"id(j) {id(j)}")
print("i = ", i)
print("j = ", j)
j[0] = 100
j[4][1] = 10000
print(f"i {i}")
print(f"i {j}")
