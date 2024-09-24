def next_permutation(nums):
    ind = -1
    n=len(nums)
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            ind = i
            break

    if ind == -1:
        nums.reverse()
        return nums

    # Step 2: Find the next greater element
    #         and swap it with nums[ind]:
    for i in range(n - 1, ind, -1):
        if nums[i] > nums[ind]:
            nums[i], nums[ind] = nums[ind], nums[i]
            break

    # Step 3: reverse the right half:
    nums[ind + 1 :] = reversed(nums[ind + 1 :])
    return nums    
nums=[1,2,3]
result=next_permutation(nums)
print(result)
