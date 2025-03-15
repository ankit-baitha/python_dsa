def search_in_rotated_array(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low + high)//2
        if arr[mid]==target:
            return mid

        if arr[low]<=arr[mid]:
            if arr[low]<=target <=arr[mid]:
                high=mid-1
            else:
                low=mid+1

        else:
            if arr[mid]<=target <=arr[high]:
                low =mid+1
            else:
                high= mid-1
arr=[5,6,7,8,9,10,11,12,1,2,3,4]
print(search_in_rotated_array(arr,6))