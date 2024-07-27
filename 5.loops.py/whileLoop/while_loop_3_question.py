""""
ask a start number from user =6
Ask a end number from user =15

6,7,8......15


ask a start number from user =15
Ask a end number from user =8

8......15

"""

start = int(input("Enter the strat number = "))
end = int(input("Enter the end number = "))

if start < end:
    while start <= end:
        print(start, end=" ")
        start += 1
else: 
    while end <= start:
        print(end, end=" ")
        end += 1

