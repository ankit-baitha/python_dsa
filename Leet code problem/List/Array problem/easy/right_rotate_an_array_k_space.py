# brute solution
""""
Time complexity =O(n*k)
space complexity=O(1)
"""

def rotate(arr,k):
    for _ in range(k):
        element=arr.pop()
        arr.insert(0,element)
    return arr
arr=[5,6,1,8,3,4,2,9]
x=rotate(arr,3)
print(x)



""""
Time complexity =O(n*(k%len(arr)))
space complexity=O(1)
"""

def rotate(arr,k):
    rotation= k % len(arr)
    for _ in range(rotation):
        element=arr.pop()
        arr.insert(0,element)
    return arr
arr=[5,6,1,8,3,4,2,9]
x=rotate(arr,3)
print(x)

""""
optimal solution
"""


def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """

    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    n = len(nums)
    k=k % n  # Handle cases where k > n

    reverse(n - k, n - 1)  # Reverse the last k element
    reverse(0, n - k - 1)  # Reverse the remaining elements
    reverse(0, n - 1)  # Reverse the entire array
    return nums
nums=[5,6,1,8,3,4,2,9]
x=rotate(nums,3)
print(x)

    
