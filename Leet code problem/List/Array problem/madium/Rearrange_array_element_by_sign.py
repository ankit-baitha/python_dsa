'''
brute solution
time complexity= O(n + n/2) ~ O(n)
space complexity = O(n)
'''
nums=[3,1,-2,-5,2,-4]
positive=[]
negative=[]
for i in range(0,len(nums)):
    if nums[i]>0:
        positive.append(nums[i])
    else:
        negative.append(nums[i])
        
for i in range(0,len(positive)):
    nums[2*i]=positive[i]
    nums[(2*i)+1]=negative[i]
print(nums)
        


'''
optimal solution
Time complexity -> O(N)
N is number of elements in nums

Space complexity -> O(N)
'''

def rearrangeArray(nums):
    n=len(nums)
    ans=[0]*n
    posIndex=0
    negIndex=1
    for i in range(n):
        if nums[i]<0:
            ans[negIndex]=nums[i]
            negIndex +=2
        else:
            ans[posIndex]=nums[i]
            posIndex +=2
    return ans
nums=[3,1,-2,-5,2,-4]
result=rearrangeArray(nums)
print(result)
        
            
    