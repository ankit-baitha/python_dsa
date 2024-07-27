set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7, 8}
set3 = set1 - set2
set3 = set2 - set1
# set3 = set1 + set2
# set3 = set1 / set2
# set3 = set1 % set2
print(set3)


set1 = {76, 43, 19, 83, 41, 33, 33, 33, 33}
print(set1)
# By index (not possible)

# By Value
for num in set1:
    print(num)

set1 = {76, 43, 19, 83, 41, 33, 33, 33, 33}
print(set1)
set1.add(100)
print(set1)
set1.remove(43)
print(set1)
another_set = set1.copy()
another_set.add(1000)
print(set1)
print(another_set)
# set1.clear()
# print(set1)
