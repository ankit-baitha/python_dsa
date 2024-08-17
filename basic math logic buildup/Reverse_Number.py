def Reverse_number(num:int)->int:
    n=num
    ruselt=0
    while n>0:
        Id=n%10
        ruselt=(ruselt *10) +Id
        n=n//10
    return ruselt
print(Reverse_number(3456765))
    