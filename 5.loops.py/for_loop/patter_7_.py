"""
1 
1 2 
1 2 3
1 2 3 4
1 2 3 4 5
"""


def pattern(n: int):

    for i in range(1, n):
        for j in range(1, i + 1):

            print(j, end=" ")
        print()


pattern(6)
