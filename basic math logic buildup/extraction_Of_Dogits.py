"""
TC=O(log10N)
SC=O(1)
"""
def Extraction_of_digits(num:int):
    n=num
    while n>0:
        Id=n%10
        print(Id)
        n=n//10
Extraction_of_digits(234534)