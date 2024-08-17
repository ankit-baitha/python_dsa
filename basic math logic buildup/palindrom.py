def palindrom(num:int)->bool:
    n=num
    result=0
    while n>0:
        id=n%10
        result=(result*10)+id
        n=n//10
    if num==result:
        return True
    else:
        return False
print(palindrom(1234321))
print(palindrom(1234321))
print(palindrom(1251))
