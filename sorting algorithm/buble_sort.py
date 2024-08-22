 # buble sorting
 
 #worst case time complexity O(n^2)
 # average case time complexity O(n^2)
def buble_sort(arr):
    n=len(arr)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        
    return arr
print(buble_sort([3,6,7,3,6,1,6]))
# method 2
def buble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        
    return arr
print(buble_sort([3,6,7,3,6,1,6]))


# best case time complexity O(n)

def buble_sort1(arr):
    n=len(arr)
    for i in range(n-2,-1,-1):
        swap=False
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
    if swap ==False:
        return arr 
print(buble_sort1([1,2,3,4,5]))

