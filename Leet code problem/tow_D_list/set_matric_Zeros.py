# 73. set matrix zeros
# problem : Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]


# battet solution
class Solution:
    def markInfinity(self, matrix, row, col):
        r = len(matrix)
        c = len(matrix[0])

        # Mark entire column 
        for i in range(r):
            if matrix[i][col] != 0:  
                matrix[i][col] = float("inf")

        # Mark entire row
        for j in range(c):
            if matrix[row][j] != 0:  
                matrix[row][j] = float("inf")

    def setZeroes(self, matrix) -> None:
        r = len(matrix)
        c = len(matrix[0])

        # First pass: mark cells that need to be zero 
        for i in range(r): #tc=(n*m)
            for j in range(c):
                if matrix[i][j] == 0:
                    self.markInfinity(matrix, i, j) #tc =0(n+m)

        # Second pass: convert all infinity marks to zero
        for i in range(r): # tc= O(n*m)
            for j in range(c):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0
mat = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(mat)
print(mat)

# time comlexiy = O(((n+m)*(n*m)) + O(n*m))
# sc = O(1)



# optimal solution
def set_zeros(matrix):
    r=len(matrix)
    c=len(matrix[0])
    rowtrack=[0 for _ in range(r)]
    coltrack=[0 for  _ in range(c)]

    for i in range(r):
        for j in range(c):
            if matrix[i][j]==0:
                rowtrack[i]=-1
                coltrack[j]=-1
    for i in range(r):
        for j in range(c):
            if rowtrack[i]==-1 or coltrack[j]==-1:
                matrix[i][j]=0
    return matrix
mat = [[1,1,1],[1,0,1],[1,1,1]]
print(set_zeros(mat))

# tc= O(2*(n*m))
# sc=(n+m)