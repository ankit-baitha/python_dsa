def maximum_ones(num):
    maximum_count=0
    count=0
    for i in range(0,len(num)):
        if num[i]==1:
            count=count+1
            
        else:
            maximum_count=max(maximum_count,count)
            count=0
    return max(maximum_count,count)
num=[0,1,1,0,1,1,1,1,1,0,0,1]
x=maximum_ones(num)
print(x)
