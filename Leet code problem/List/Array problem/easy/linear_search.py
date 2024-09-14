""""
question 

Our intent is to search for a specific element num in an array arr using a linear search algorithm. The goal is to determine the index of num in arr if it exists; otherwise, return -1 indicating that the element is not found in the array.
time complexity =O(n)
space complexity = O(1)
"""
def linear_search(nums,target):
    for i in range(0,len(nums)):
        if nums[i]==target:
            return i
    return -1
nums=[3, 5, 1, 2, 9]
x=linear_search(nums,2)
print(x)


