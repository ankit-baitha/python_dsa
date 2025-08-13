# linear time
# time complexity = 0(N)

def count_occurrences(arr,target):
    count=0
    for i in range(0,len(arr)):
        if target==arr[i]:
            count +=1
    return count
arr=[1,1,1,1,2,3,4,6,6,6,6,8,9,14]
print(count_occurrences(arr,1))






