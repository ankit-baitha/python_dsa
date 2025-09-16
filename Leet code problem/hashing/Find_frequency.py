'''
Given an array arr of positive integers and an integer x. Return the frequency of x in the array.
example
Input: arr = [1, 1, 1, 1, 1], x = 1
Output: 5
Explanation: Frequency of 1 is 5.
'''
def fincFrequency(arr,x):
    Count =0
    for num in arr:
        if num ==x:
            Count +=1
    return Count
arr= [1, 2, 3, 3, 2, 1]
ans =fincFrequency(arr,2)
print(ans)

