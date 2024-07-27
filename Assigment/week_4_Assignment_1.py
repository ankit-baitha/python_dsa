# # Make the follwing pattern
# # Ask n from user which means number of lines to print


# pattern 1
""""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""


def pattern_1(n: int):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print(" ")


5
# pattern 2
""""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""


def pattern_2(n: int):
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print(" ")


# n = int(input("enter the lines = "))
# pattern_2(n)


# pattern 3
""""
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
"""


def pattern_3(n: int):
    for i in range(n, 0, -1):
        for j in range(i, n + 1):
            print(j, end=" ")
        print(" ")


# n = int(input("enter the lines = "))
# pattern_3(n)


# Pattern 4
"""""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""


def pattern_4(n: int):
    for i in range(1, n + 1):
        for j in range(5, n - i, -1):
            print(j, end=" ")
        print(" ")


# n = int(input("enter the lines = "))
# pattern_4(n)


# pattern 5
""""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""


def pattern_5(n: int):
    for i in range(1, n + 1):
        for j in range(5, i - 1, -1):
            print(j, end=" ")
        print(" ")


# n = int(input("enter the lines = "))
# pattern_5(n)


# pattern 6
""""
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
"""


def pattern_6(n: int):
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print(j, end=" ")
        print(" ")


# n = int(input("enter the lines = "))
# pattern_6(n)


# pattern 7

""""
5 4 3 2 1  
4 3 2 1  
3 2 1
2 1
1
"""


def pattern_7(n: int):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print(" ")


# n = int(input("enter the lines = "))
# pattern_7(n)


# pattern 8

""""
1
2 3
4 5 6
7 8 9 10 
11 12 13 14 15
"""


def pattern_8(n=int):
    number = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(number, end=" ")
            number += 1
        print()


n = int(input("enter the lines = "))
pattern_8(n)


# pattern 9
""""
1
1 2
1 2 1
1 2 1 2 
1 2 1 2 1
"""


def pattern_9(n=int):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            # print(j, end=" ")
            if i % 2 == 0:
                print(2, end=" ")
            else:
                print(1, end=" ")
        print(" ")


# n = int(input("enter the lines = "))
# pattern_9(n)


# pattern 10
"""
1 2 3 4 5
1 2 3 4
1 2 3  
1 2
1
"""


def pattern_10(n: int):
    for i in range(1, n + 1):
        for j in range(1, n - i + 2):
            print(j, end=" ")
        print(" ")


# n = int(input("enter the lines = "))
# pattern_10(n)
