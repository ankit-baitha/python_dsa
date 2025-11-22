'''
brute solution
tc = O(n^2)
sc = O(1)
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


# butter solution.
def longestConsecutive_sequence_2(nums):
    nums.sort()
    Count =0
    last_smaller= float('-inf')
    longest =0
    n=len(nums)
    for i in range(0,n):
        num=nums[i]
        if num-1==last_smaller:
            Count +=1
            last_smaller =num
        elif nums!= last_smaller:
            Count =1  
            last_smaller =num
        longest =max(Count,longest)
    return longest
nums=[100,4,200,1,3,2]
print(longestConsecutive_sequence_2(nums))

# tc =O(nlogn + n)
# sc = O(1)

# optimal solution.

def longestConsecutive_sequence_3(nums):
    my_set = set()
    for i in range(0,len(nums)):
        my_set.add(nums[i])
    longest = 0
    for num in my_set:
        if num-1 not in my_set:
            x=num
            Count = 1
            while x + 1 in my_set:
                Count +=1
                x+=1
            longest = max(longest,Count)
    return longest
nums=[100,4,200,1,3,2]
print(longestConsecutive_sequence_2(nums))    

# tc = O(n + n +n)

# sc = O(n)