"""

"""

for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for k in range(5, 5 - i, -1):
        print(k, end=" ")
    print()
    
# method 2

for a in range(5, 0, -1):
    for b in range(1, a):
        print(" ", end=" ")
    for c in range(5, a - 1, -1):
        print(c, end=" ")

    print()
