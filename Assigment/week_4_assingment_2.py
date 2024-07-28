"""
Ask n from user which means number of lines to print
example n=5


        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
"""

n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1 - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()


"""


        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1
"""
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1 - i, 1):
        print(" ", end=" ")
    for k in range(i, 0, -1):
        print(k, end=" ")
    print()


""""


        5
      5 4
    5 4 3
  5 4 3 2
5 4 3 2 1
"""
n = int(input())
for i in range(n, 0, -1):
    for j in range(1, i):
        print(" ", end=" ")
    for k in range(5, i - 1, -1):
        print(k, end=" ")
    print()

""""
        5
      4 5
    3 4 5
  2 3 4 5
1 2 3 4 5
"""
n = int(input())
for i in range(n, 0, -1):
    for j in range(1, i):
        print(" ", end=" ")
    for k in range(i, n + 1):
        print(k, end=" ")
    print()

""""
        5
      4 4
    3 3 3
  2 2 2 2
1 1 1 1 1
"""
n = int(input())
for i in range(n, 0, -1):
    for j in range(1, i):
        print(" ", end=" ")
    for k in range(i, n + 1):
        print(i, end=" ")
    print()

"""
          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
* * * * * * * * * * *
"""
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1 - i):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print("*", end=" ")
    print()

"""
        5
      4 4 4
    3 3 3 3 3
  2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 1
"""
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1 - i):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print(6 - i, end=" ")
    print()

""""
          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
* * * * * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *
"""
n = int(input())
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
""""
        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4 
5 5 5 5 5 5 5 5 5
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1
"""

n = int(input())
for i in range(1, n // 2 + 1 + 1):
    for j in range(1, n // 2 + 1 + 1 - i):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print(i, end=" ")
    print()
for a in range(n // 2, 0, -1):
    for b in range(1, n // 2 + 1 - a + 1):
        print(" ", end=" ")
    for c in range(1, a * 2):
        print(c, end=" ")
    print()

# method 2
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print(i, end=" ")
    print()
for a in range(4, 0, -1):
    for b in range(1, 6 - a):
        print(" ", end=" ")
    for c in range(1, a * 2):
        print(1)
    print()
