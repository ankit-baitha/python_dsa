

# how to represent 2D list

nums=[[5,2,3],[7,6,9],[1,9,5]]

rows=len(nums)
col = len(nums[0])
for i in range(0,rows):
    for j in range(0,col):
        print(nums[i][j],end="  ")
    print()
print()
# print(nums[1][1])


# 1 print  upper triangle
 
for i in range(0,rows):
    for j in range(0,col):
        if j>=i:
            print(nums[i][j],end=" ")
        else:
            print("*",end = " ")
    print()

print()
# 2 print lower triangle
for i in range(0,rows):
    for j in range(0,col):
        if i>=j:
            print(nums[i][j], end=" ")
        else:
            print("*",end=" ")
    print()
print()

# 3 print diagonal 
for i in range(0,rows):
    for j in range(0,col):
        if i==j:
            print(nums[i][j], end=" ")
        else:
            print("*",end=" ")
    print()
print()



# transpose of matrix

nums=[[5,2,3],[7,6,9],[1,9,5]]
rows=len(nums)
cols= len(nums[0])
result = [ [0]*rows for _ in range(cols)]
print(result)
for i in range(0,rows):
    for j in range(0,cols):
        result[j][i]=nums[i][j]
print(result)
