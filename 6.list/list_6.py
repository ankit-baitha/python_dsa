# print all prime number


# def is_prime_number(num: int) -> bool:
#     factors = 0
#     for i in range(1, num + 1):
#         if num % 1 == 0:
#             factors += i
#     if factors == 2:
#         return True
#     return False


# my_list = [45, 31, 7, 5, 3, 17, 19, 25, 65, 92]
# n = len(my_list)
# for index in range(0, n):
#     if is_prime_number(my_list[index]) == True:
#         print(my_list[index], end=" ")

my_list = [45, 31, 7, 5, 3, 17, 19, 25, 65, 92]
for num in my_list:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        print(num, end=" ")


# hard
my_list_1 = [4, 8, 6, 5, 3, 12, 1, 7, 6, 2]
for num in my_list_1:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
