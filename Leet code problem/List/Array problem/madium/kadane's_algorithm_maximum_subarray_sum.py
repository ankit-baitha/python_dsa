'''
brute solution
time complexity =O(n^2)
space complexity = O(1)
'''
def maximum_subarray(nums):
    maxi=float("-inf")
    n=len(nums)
    for i in range(0,n):
        total=0
        for j in range(i,n):
            total +=nums[j]
            maxi=max(maxi,total)
    return maxi
nums=[-2,1,-3,4,-1,2,1,-5,4]
result= maximum_subarray(nums)
print(result)

'''
'''
def kadane(nums):
    maxi = float("-inf")
    total=0
    for i in range(0,len(nums)):
        total +=nums[i]
        maxi=max(maxi,total)
        
        if total>maxi:
            maxi = total
        
        if total <0:
            total=0
    return maxi
nums=[-2,1,-3,4,-1,2,1,-5,4]
result= kadane(nums)
print(result)
