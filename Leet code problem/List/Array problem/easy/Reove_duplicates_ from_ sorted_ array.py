
"""
Time complexity = O(n) where n is the number of elements in list
We are looping two different times, so it will be O(n) + O(n).
Which equals tos O(n)

Space complexity = O(n), suppose all numbers are unique, it will take same length as list
"""

def remove_duplicates(arr):
    n=len(arr)
    dictionary={}
    for i in range(0,n):
        dictionary[arr[i]]=0
    j=0
    for key in dictionary:
        arr[j]=key
        j+=1
        
    return j
    
    
arr=[0,0,1,1,1,2,2,3,3,4]
x=remove_duplicates(arr)
print(x)

#optimal solution

"""
Time complexity = O(n) where n is the number of elements in list
But in this case, we are using only 1 loop instead of 2 FOR loops

Space complexity = O(1), no extra space
"""
def remove_duplicate(arr):
    if len(arr)==1:
        return 1
    i=0
    j=i+1
    while j<len(arr):
        if arr[i]!=arr[j]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
        
    return i+1
arr=[0,0,1,1,1,2,2,3,3,4]
x=remove_duplicate(arr)
print(x)


