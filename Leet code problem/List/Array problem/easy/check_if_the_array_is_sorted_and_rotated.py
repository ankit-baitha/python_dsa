def sort_to_rotated(arr):
    n=len(arr)
    rotations=0
    for i in range(0,n-1):
        if arr[i]>arr[(i+1)%n]:
            rotations +=1
        if rotations>1:
            return False
    return True
arr = [3, 1, 4, 1, 5, 9]
x=sort_to_rotated(arr)
print(x)