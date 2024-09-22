# count factor question

def print_factors(num: int) -> None:
    i = 1
    c1 = 0
    while i <= num:
        if num % i == 0:
            c1 = c1 + 1
            print(i, end=" ")
        i += 1
    print("count the factor : ", c1)


num = int(input("enter the number : "))
print_factors(num)


def print_factors_2(num: int) -> None:
    i = 1
    c1 = 0
    while i <= num // 2:
        if num % i == 0:
            c1 = c1 + 1
            print(i, end=" ")
        i += 1
    print(num)
    print("count the factor : ", c1+1)


num = int(input("enter the number : "))
print_factors_2(num)
