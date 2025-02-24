def contains_duplicate(nums: list[int]):
    hashset= set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False
contains_duplicate([1,2,3,1])
