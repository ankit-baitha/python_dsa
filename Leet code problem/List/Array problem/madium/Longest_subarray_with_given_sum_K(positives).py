''''
time complexity= O(N^3)
space comlexity = o(1)
'''

arr=[1,2,3,1,1,1,1,3,3]
x=3
n=len(arr)
maximum_length=0
for i in range(0,n):
    for j in range(i,n):
        total=0
        for k in range(i, j+1):
            total +=arr[k]
        if x==total:
            maximum_length = max(maximum_length, j-i+1)
print(maximum_length)        


''''
time complexity= O(N^2)
space comlexity = O(1)
'''

arr=[1,2,3,1,1,1,1,3,3]
x=3
n=len(arr)
maximum_length=0
for i in range(0,n):
    total=0
    for j in range(i,n):
            total +=arr[j]
            if x==total:
                maximum_length = max(maximum_length, j-i+1)
print(maximum_length)         


''''
optimal solution 
time complexity= O(N)
space comlexity = O(N)
'''
arr=[1,2,3,1,1,1,1,3,3]
k=3


sum_map={}
sum=0
maximum_length=0

for i in range(0,len(arr)):
    sum +=arr[i]
    if sum==k:
        maximum_length = i+1
        
    remaining = sum - k
    
    if remaining in sum_map:
        l=i-sum_map[remaining]
        maximum_length=max(maximum_length,l)
    if sum not in sum_map:
        sum_map[sum]=i
print(maximum_length)
    
    
        

        