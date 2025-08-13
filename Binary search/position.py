class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
 
        low = self.lower_bound(nums,target)
        high= self.upper_bound(nums,target)
        if low <=high:
            return [low,high]
        else:
            return [-1,-1]
    
    def lower_bound(self, nums,target):
        left=0
        right=len(nums)-1
        while left <=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
 
    def upper_bound(self, nums,target):
        left=0
        right=len(nums)-1
        while left <=right:
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return right
 
 
nums = [5,7,7,8,8,10]
target = 8
 
 # print(Solution().searchRange(nums,target))
 
 # method 2
def binary_search_left(nums,target):
    ans=-1
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low + high)//2
        if nums[mid]==target:
            ans=mid
            high = mid -1
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid + 1
    return ans
nums = [5,7,7,8,8,10]
target = 8
 
 
def binary_search_right(nums,target):
    ans=-1
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low + high)//2
        if nums[mid]==target:
            ans=mid
            low = mid+1
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid + 1
    return ans
left=binary_search_left([5,7,7,8,8,10],8)
right=binary_search_right([5,7,7,8,8,10],8)
print([left,right])