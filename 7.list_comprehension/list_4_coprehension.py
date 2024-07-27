"""""
1,3,5,7,9 -> odd
2,4,6,8 -> even
"""

# what to add                    when to add
my_lis = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)]
print(my_lis)
