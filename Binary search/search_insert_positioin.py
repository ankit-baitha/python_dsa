def search_insert_position(nums,target):
    low=0
    high=len(nums)-1
    ans=len(nums)
    while low<=high:
        mid=(low + high)//2
        if nums[mid]>=target:
            ans=mid
            high = mid - 1
        else:
            low=mid+1
    return ans
print(search_insert_position([1,3,5,6],7))



