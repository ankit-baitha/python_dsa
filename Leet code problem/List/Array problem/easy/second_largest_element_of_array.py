# second largest and second smallest number
# brust solution
def second(arr):
    n=len(arr)
    arr.sort()
    return arr[n-2],arr[1]
arr=[3,5,-2,4,-64,34,6,234,5,-323]
x=second(arr)
print(f"second largest and smallest element ={x}")

# optimalm solution
def second_largest_element(arr):
    n=len(arr)
    maxi=float("-inf")
    second_maxi=float("-inf")
    mini=float("inf")
    second_mini=float("inf")
    for i in range(0,n):
        if arr[i]>maxi:
            maxi=arr[i]
        if arr[i]<mini:
            mini=arr[i]
    for i in range(0,n):
        if arr[i]>second_maxi and arr[i]!=maxi:
            second_maxi=arr[i]
        if arr[i]<second_mini and arr[i]!=mini:
            second_mini=arr[i]
        
    print("second maximum number ",second_maxi)
    print("second minimum number ",second_mini)
arr=[3,5,-2,4,-64,34,6,234,5,-323]
second_largest_element(arr)


# optimal solution
def second_maxi_element(arr):
    n=len(arr)
    maxi=float('-inf')
    second_maxi=float("-inf")
    for i in range(0,n):
        if arr[i]>maxi:
            second_maxi=maxi
            maxi=arr[i]
        elif arr[i]>second_maxi and arr[i]!=maxi:
            second_maxi=arr[i]
    print("second maximum number ",second_maxi)
arr=[3,5,-2,4,-64,34,6,234,5,-323]
second_maxi_element(arr)
