'''
brute solution

time complexity O(nlong n)
space complexity = O(1)
'''
def sortcolor(nums):
    nums.sort()
    return nums
nums=[1,1,0,2,1,0,0,2,2,1,2]
result=sortcolor(nums)
print(result)

'''
better solution
time complexit = O(n + n)= O(2n)
space complexity = O(1)

'''
def sortcolor1(nums):
    n=len(nums)
    cont1=0
    cont2=0
    cont3=0
    for i in range(0,n):
        if nums[i]==0:
            cont1 +=1
        elif nums[i]==1:
            cont2 +=1
        else:
            cont3 +=1
    
    for i in range(0,cont1):
        nums[i]=0

    for i in range(cont1,cont1+cont2):
        nums[i]=1
    for i in range(cont1+cont2,n):
        nums[i]=2
    return nums
nums=[1,1,0,2,1,0,0,2,2,1,2]
result=sortcolor1(nums)
print(result)

'''
optimal solution


'''

def sortColors( nums):
    low = 0
    mid = 0
    high = len(nums) - 1


    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums
nums=[1,1,0,2,1,0,0,2,2,1,2]
result=sortColors(nums)
print(result)

        

        