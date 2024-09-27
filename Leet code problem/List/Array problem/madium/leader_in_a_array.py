"""
time complexity = O(n)
space complexity = O
"""

def leader_in_array(nums):
    n=len(nums)
    leader=[]
    maxi=float("-inf")
    for i in range(n-1,-1,-1):
        if nums[i]>=maxi:
            leader.append(nums[i])
            maxi=nums[i]
    return leader[::-1]
nums=[16, 17, 4, 3, 5, 2]
print(leader_in_array(nums))