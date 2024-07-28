"""
extrection of digits
"""


def extrection_of_digits(num: int) -> None:
    n = num
    while n > 0:
        digit = n % 10
        print(digit, end="")
        n = n // 10


num = int(input())
extrection_of_digits(num)


# count digits
def count_digit(num: int) -> None:

    n = num
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    print(count)


num = int(input())
count_digit(num)


"""
check palindrom

"""


def check_palindrom(num: int) -> bool:
    n = num
    result = 0
    while n > 0:
        digit = n % 10
        result = (result * 10) + digit
        n = n // 10
    return num == result


num = int(input())
print(check_palindrom(num))

""""
armstrong number
"""


def armstrong_number(num: int) -> int:
    n = num
    l = len(str(num))
    print(l)
    total = 0
    while n > 0:
        digit = n % 10
        total = total + (digit**l)
        n = n // 10
    return num == total


num = int(input("enter the number = "))
print(armstrong_number(num))
