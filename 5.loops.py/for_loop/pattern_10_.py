"""""
        * 
      * *     
    * * *     
  * * * *     
* * * * * 
"""

for i in range(1, 6):
    for j in range(1, 5 - i + 1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print("*", end=" ")

    print()


def pattern_2(n: int):

    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" ", end=" ")
        for k in range(1, i + 1):
            print("*", end=" ")

        print()


n = int(input("enter the numbr : "))
pattern_2(n)
