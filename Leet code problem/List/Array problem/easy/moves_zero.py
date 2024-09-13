"""
brute solution 
time complexity= O(n)
space complexity =O(n)
"""
# right sift zero
def Move_zeros(nums):
    non_zero_list=[]
    n=len(nums)
    for i in range(0,n):
        if nums[i] !=0:
            non_zero_list.append(nums[i])
    
    nzl=len(non_zero_list)
    for i in range(0,nzl):
        nums[i]=non_zero_list[i]
    
    for i in range(nzl,n):
        nums[i]=0
    return nums
nums=[1,0,2,3,2,0,0,4,5,1]
x=Move_zeros(nums)
print("Right sift zeros ", x)


#left sift zero
def sortColors(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
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
                
nums=[1,0,2,3,2,0,0,4,5,1]
x=sortColors(nums)
print("Left sift zeros", x)



""""
optimal s
time complexity = O(n)
space complexity =O(n)
"""
# right sift zeros
def move(nums):
    if len(nums)==1:
        return 
    i=0
    while i<len(nums):
        if nums[i]==0:
            break
        i +=1
    j=i+1
    while j<len(nums):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i +=1
        j +=1
    return nums


nums=[0,1,0,3,12]
x=move( nums)
print("right sift zeros",x)

