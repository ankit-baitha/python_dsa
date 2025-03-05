def floor_ciel(nums,target):
    low=0
    high=len(nums)-1
    floor=-1
    ceil=-1
    while low<=high:
        mid=(low + high)//2
        if nums[mid]==target:
            return [nums[mid],nums[mid]]
        elif nums[mid]>target:
            ceil=nums[mid]
            high=mid-1
        else:
            floor=nums[mid]
            low=mid+1
    return [floor,ceil]
print(floor_ciel([3, 4, 4, 7, 8, 10]  ,2))        