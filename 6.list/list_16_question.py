""""
ask a number from user =6
enter element = 4
enter element = 5
enter element = 5
enter element = 6
enter element = 2
enter element = 7
"""

my_list = []
for i in range(1, 7):
    number = int(input(f"enter the element {i}  = "))

    my_list.append(number)
print(my_list)

# from typing import List


# def create_list(length: int) -> List[int]:
#     my_list1 = []
#     for i in range(length):
#         x = int(input(f"enter elements {i+1} = "))
#         my_list1.append(x)
#     return my_list1


# lst = create_list(6)
# print(lst)
