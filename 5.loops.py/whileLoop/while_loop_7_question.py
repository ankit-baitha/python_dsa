"""
start end / 100 total of all  even number 
1 to 100
"""

start = int(input("enter the start of values: "))
end = int(input("enter the end of values: "))
total = 0
while start <= end:
    if start % 2 == 0:
        total = total + start
    start += 1
print(total)
