"""
Time complexity = O(n)
Space complexity = O(1)
"""

def rotate_one_place(arr):
    last_element=arr.pop()
    arr.insert(0,last_element)
    
    return arr
arr=[5,9,8,1,8,6,1]
x=rotate_one_place(arr)
print(x)

