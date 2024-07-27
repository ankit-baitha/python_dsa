"""

keep asking a number user util he enters zero(0)
calculate total
"""

total = 0
while True:
    num = int(input("Enter the number : "))
    if num == 0:
        break
    total = total + num
print(total)
