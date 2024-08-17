def Armstrong_number(num:int)->bool:
    n=num
    l=len(str(num))
    result=0
    while n>0:
        id=n%10
        result=result + (id **l)
        n=n//10
    if result==num:
        return True
    else:
        return False
print(Armstrong_number(153))
    