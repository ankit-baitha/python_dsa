""""
 368 
 factors -> total
"""


def factors(num):
    i = 1
    count = 0
    total = 0
    while i <= num:
        if num % i == 0:
            count += 1
            total = total + i
            print(i, end=" ")
        i += 1
    print("count = ", count)
    print("total = ", total)


num = int(input("enter then number : "))
factors(num)


# def


def factors(num):
    i = 1
    total = 0
    while i <= num:
        if num % i == 0:
            total = total + i
        i += 1
    return total


print(factors(386))
