"""
time complexity =O(n)
space complexity =0(1)
"""

def sorted_array(arr):
    n=len(arr)
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            return False
    return True
arr = [3, 1, 4, 1, 5, 9]
x=sorted_array(arr)
print(x)

