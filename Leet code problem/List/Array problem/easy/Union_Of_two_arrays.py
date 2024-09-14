"""
Time Complexity: O(n+m)
Space Complexity: O(n+m)
"""
def merge_2_sorted_arrays(left,right):
    merge=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            if len(merge)==0 or merge[-1] !=left[i]:
                
                merge.append(left[i])
            i+=1
        else:
            if len(merge)==0 or merge[-1]!=right[j]:
                
                merge.append(right[j])
            j+=1
            
    while i<len(left):
        if len(merge)==0 or merge[-1] !=left[i]:
            merge.append(left[i])
        i+=1
    while j<len(right):
        if len(merge)==0 or merge[-1] !=right[j]:
            merge.append(right[j])
        j+=1
    print(merge)
left=[1,2,2,3,5,5,5,6,7]
right=[1,2,3,3,7,7,8,8,9,10]
merge_2_sorted_arrays(left,right)
            