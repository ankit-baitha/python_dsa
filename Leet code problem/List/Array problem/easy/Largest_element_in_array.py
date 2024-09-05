# brute solution
"""
Time complexity = O(N logN) where N is the number of elements in list
Space complexity = O(1)
"""


def largest_element(arr):
    arr.sort()
    return arr[-1]
arr=[3,5,-2,4,-64,34,6,234,5,-323]
x=largest_element(arr)
print(f"largest element ={x}")


#optimal solution
"""
Time complexity = O(N) where N is the number of elements in list
Space complexity = O(1)
"""
def largest_element_1(arr):
    maxi=float("-inf")
    n=len(arr)
    for i in range(0,n):
        if arr[i]>maxi:
            maxi=arr[i]
    return maxi
arr=[3,5,-2,4,-64,34,6,234,5,-323]
x=largest_element_1(arr)
print(f"largest element ={x}")

