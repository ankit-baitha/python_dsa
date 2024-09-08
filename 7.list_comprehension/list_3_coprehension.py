# [2, 4, 6, 8, 10]
# my_list = [i for i in range(1, 11) if i % 2 == 0]
# print(my_list)


def prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


my_list1 = [i for i in range(1, 100) if prime(i)]
print(my_list1)


