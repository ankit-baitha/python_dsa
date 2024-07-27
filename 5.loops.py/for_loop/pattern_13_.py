""""
        *
      * * *        
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

n = int(input("enter the number : "))
for i in range(1, n // 2 + 1 + 1):
    for j in range(1, n // 2 + 1 + 1 - i):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print("*", end=" ")
    print()
for a in range(n // 2, 0, -1):
    for b in range(1, n // 2 + 1 - a + 1):
        print(" ", end=" ")
    for c in range(1, a * 2):
        print("*", end=" ")
    print()


# method 2
n = int(input("enter the number : "))
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print("*", end=" ")
    print()
for a in range(4, 0, -1):
    for b in range(1, 6 - a):
        print(" ", end=" ")
    for c in range(1, a * 2):
        print("*", end=" ")
    print()
