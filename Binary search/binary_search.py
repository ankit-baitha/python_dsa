"""
binary search  
"""
def binary_search(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid= (low + high)//2
        if nums[mid]==target:
            return mid
        elif target <nums[mid]:
            high =mid-1
        else:
            low = mid + 1
    return -1
nums=[2,4,6,7,10,11,16,18]
result=binary_search(nums,6)
print(result)
'''
by recursion
'''
def binary_search1(nums, low ,high,target):
    if low>high:
        return -1
    mid=(low + high)//2
    if nums[mid]==target:
        return mid
    elif target < nums[mid]:
        return binary_search1(nums,low,mid-1,target)
    else:
        return binary_search1(nums,mid+1,high,target)
    
nums=[2,4,6,7,10,11,16,18]
result=binary_search1(nums,0,len(nums)-1,6)
print(result)