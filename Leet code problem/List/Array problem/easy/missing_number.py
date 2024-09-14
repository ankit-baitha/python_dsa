"""
brute solution
time complexity =O(N^2)
space complexity = O(1)

"""
def missing_number(arr):
    for i in range(0,len(arr)+1):
        if i not in arr:
            return i
arr=[9,6,4,2,3,5,7,0,1]
x=missing_number(arr)
# print(x)



""""
better solution
tc = O(3N) ~ O(N)
sc = O(N)

"""
def missing(arr):
    n=len(arr)
    dict={}
    for i in range(0,n+1):
        dict[i]=0
    print(dict)
    for i in range(0,n):
        dict[arr[i]]=1
    print(dict)
    for k,v in dict.items():
        if not v:
            return k
arr=[9,6,4,2,3,5,7,0,1]
x=missing(arr)
print(x)   


"""
Optimal solution

"""
def Missing(arr):
    n=len(arr)
    original_total=(n*(n+1))//2
    return original_total - sum(arr)
arr=[9,6,4,2,3,5,7,0,1]
x=Missing(arr)
# print(x)   

