'''
brute solution
'''
def longestConsecutive_sequence(nums):
    n=len(nums)
    maxi_count=0
    for num in nums:
        Count=1
        x =num
        while x+1 in nums:
            Count +=1
            x=x+1
        maxi_count=max(maxi_count,Count)
    return maxi_count
nums=[100,4,200,1,3,2]
print(longestConsecutive_sequence(nums))