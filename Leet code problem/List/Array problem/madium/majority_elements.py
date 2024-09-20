'''
brute solution
time complexity = O(N)
space complexity = O(1)

'''
def majority(nums):
    n=len(nums)
    for i in range(0,n):
        Count=0
        for j in range(0,n):
            if nums[j]==nums[i]:
                Count +=1
        if Count >n//2:
            return nums[i]
        
nums = [2,2,1,1,1,2,2]
result = majority(nums)
print(result)


'''
better solution
time complexity = O(n + n/2) ~~ O(n)
space complexit = O(n/2) ~ O(n)
'''
def majorityElement( nums):
    n = len(nums)
    hash_map = dict()
    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1

    for num, freq in hash_map.items():
        if freq > n // 2:
            return num 
nums = [2,2,1,1,1,2,2]
result = majorityElement(nums)
print(result)

'''
optimal solution
time complexity= O(n)
time comlexity= O(n)

'''
def majorityElement1( nums):
    n = len(nums)
    count = 0
    ele = float("-inf")
    for i in range(n):
        if count == 0:
            count = 1
            ele = nums[i]
        elif nums[i] == ele:
            count += 1
        else:
            count -= 1

        # Verify if it is the majority
    count = 0
    for i in range(n):
        if nums[i] == ele:
            count += 1

    if count > n // 2:
        return ele
    return -1

nums = [2,2,1,1,1,2,2]
result = majorityElement1(nums)
print(result)

