# merge two sorted lists
def merge_sorted_list(nums1,nums2):
    n=len(nums1)
    m=len(nums2)
    result=[]
    i=0
    j=0
    while i<n and j<m:
        if nums1[i]<=nums2[j]:
            if result[-1]!=nums1[i] or len[result]==0:
                result.append(nums1[i])
            i+=1
        else:
            if len(nums2[j])==0 or result[-1]!=nums2[j]:
                result.append(nums2[j])
            j+=1
    while i<n:
        if result[-1]!=nums1[i] or len(result)==0:
            result.append(nums1[i])
        i+=1
    while j<m:
        if result[-1]!=nums2[j] or len(result)==0:
            result.append(nums2[j])
        j+=1
    return result
x=merge_sorted_list([1,2,3,0,0,0],[2,5,6])
print(x)
                

