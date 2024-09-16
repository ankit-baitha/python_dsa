'''
Brute solutio
time complexity=O(n^2)
space complexity=O(1)

'''
def find_the_number_that_oppears_ones(nums):
    n=len(nums)
    for i in range(0,n):
        count=0
        for j in range(0,n):
            if nums[i]==nums[j]:
                count +=1
        if count==1:
            return nums[i]
nums=[5,1,5,2,1,2,3,4,3]
result=find_the_number_that_oppears_ones(nums)
print(result)


'''
time complexity=O(N +n/2)~O(N)
space complexity=O(N/2)

'''
my_list = [5,1,5,2,1,2,3,4,3]


my_dict = {}
for num in my_list:
    if num in my_dict:
        my_dict[num] = my_dict[num] + 1
    else:
        my_dict[num] = 1
print(my_dict)

for key in my_dict:
    if my_dict[key]==1:
        print(key)