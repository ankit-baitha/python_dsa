# count digits of number
"""
TC=O(log10N)
SC=O(1)
"""
def count_digits(num:int)->int:
    n=num
    count=0
    while n>0:
        count+=1
        n=n//10
    return count
print("count of digits = ",count_digits(34566))
# optimal solution 
"""
TC=O(1)
SC=O(1)
"""
import math
def count_digits1(num:int)->int:
    return math.floor(math.log10(num)+1)
print(count_digits1(34567))