
nums=[[5,2,3],[7,6,9],[1,9,5]]
rows=len(nums)
cols= len(nums[0])
result = [ [0]*rows for _ in range(cols)]
print(result)
for i in range(0,rows):
    for j in range(0,cols):
        result[j][i]=nums[i][j]
print(result)
