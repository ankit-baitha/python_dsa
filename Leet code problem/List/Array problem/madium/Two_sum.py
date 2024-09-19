'''
brute solution

time comlexity = O(N(N + 1))/2 ~ O(N^2)
space complexity = O(1)

'''
def twoSum(num,target):
    n=len(num)
    for i in range(0,n):
        for j in range(i+1,n):
            if num[i] + num[j]==target:
                return [i,j]
num=[1,3,4,6,7,7,3,7]
result=twoSum(num,14)
print(result)
        
'''
better solution
but  for position is optimal
time comlexity = O(N)
space complexity = O(N)

'''
    
def Twosum(num,target):
    n=len(num)
    hash_map=dict()
    for i in range(0,n):
        remaining=target - num[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        
        hash_map[num[i]]=i

num=[1,3,4,6,7,7,3,7]
result=Twosum(num,14)
print(result)
        
'''
optimal return true and false
time complexity = O(nlog n + n) ~ 0(nlog n)
space complexity = O(1)
'''

    
def Twosum1(num,target):
    n=len(num)
    num.sort()
    left=0
    right=n-1
    while left<right:
        if num[left] +num[right]==target:
            return True
        if num[left] + num[right] >target:
            right -=1
        else:
            lef -=1
            
    return False
num=[1,3,4,6,7,7,3,7]
result=Twosum1(num,14)
print(result)
        