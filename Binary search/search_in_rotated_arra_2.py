def search_in_rotated_array_II(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low + high)//2
        if arr[mid]==target:
            return True
        if arr[low]==arr[mid]==arr[high]:
            low +=1
            high -=1
            continue
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

        return False
arr=[2,5,6,0,0,1,2]
print(search_in_rotated_array_II(arr,3))