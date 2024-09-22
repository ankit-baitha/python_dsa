# check prime number
def count_factor(num: int) -> int:
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1
    return count


# num=int(input("enter the number"))


def chek_prime(num: int) -> bool:
    factors = count_factor(num)
    if factors == 2:
        return True
    else:
        return False

print(chek_prime(10))
print(chek_prime(11))
