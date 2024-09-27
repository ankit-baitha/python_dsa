def higher_bound(arr,target):
    low=0
    high=len(arr)-1
    id =len(arr)
    while low<=high:
        mid =(low + high)//2
        if target<arr[mid]:
            id=mid
            high=mid-1
        else:
            low=mid +  1
    print(id)
arr=[1, 2, 4, 4, 4, 6, 7]
higher_bound(arr,6)