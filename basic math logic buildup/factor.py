""""
TC=-O(N)
SC= O(k) k would be the  factors of numbe

"""
from typing import List
def factors(num:int)->List[int]:
    result=[]
    for i in range(1,num+1):
        if num%i==0:
            result.append(i)
    return result
print(factors(8))

"""
better solution
TC=-O(N/2) =O(n)
SC= O(k) k would be the  factors of numbe
"""
from typing import List
def factors1(num:int)->List[int]:
    result=[]
    for i in range(1,(num//2)+1):
        if num%i==0:
            result.append(i)
    result.append(num)
    return result
print(factors1(8))

"""
optimal solution
TC = O(sqrt N) + (NlogN)
SC = O(k)
"""
from typing import List
from math import sqrt
def factors2(num:int)->List[int]:
    result=[]
    for i in range(1,int(sqrt(num))+1):  # TC  = O(sqrt N)
        if num%i==0:
            result.append(i)
            if num//i!=i:
                result.append(num//i)
    result.sort()                     # TC=O(NlogN)
    return result
print(factors2(36))
