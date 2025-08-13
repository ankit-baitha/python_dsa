def Two_sum_zero(num):
    n=len(num)
    hash_map=dict()
    for i in range(0,n):
        remaining=0 - num[i]
        if remaining in hash_map:
            return [remaining,num[i]]
        
        hash_map[num[i]]=i

num=[-1, 0, 1, 2, -1, -4]
result=Two_sum_zero(num)
print(result)