"""""
5674
10
"""

i = 5674
j = 10983
count = 0
while i <= j:
    if i % 7 == 0:
        count += 1
    i += 1

print(count)


a = 5674
b = 10983
count_1 = 0
while a <= b:
    if a % 2 == 0 and a % 7 == 0:
        count_1 = count_1 + 1

    a += 1

print(count_1)
