# pass by reference 
#  mutable object (list,dic.....) is a pass by reference
# inmutable object (int, string,float....)

def printing_list(lst: int) -> None:
    lst[0] = 1000


my_list = [2, 4, 5, 3, 3, 5, 34, 64]
print(my_list)
printing_list(my_list)
print(my_list)
