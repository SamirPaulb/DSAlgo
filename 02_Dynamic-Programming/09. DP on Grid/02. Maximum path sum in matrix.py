# https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1#

# ------------------------------------------------ Method 1 --------------------------------------------------------------------------------

# Traversing from bottom-right most to top-left most corner
class Solution:
    def maximumPath(self, N, Matrix):
        
        # AS ALL MOVES IS [r+1] DOWNWARD => SO WE HAVE TO FILL matrix ROW WISE
        # => in a row fill the whole row from right to left then go to the above row
        
        res = 0
        
        def get(i, j):  # to get value from Matrix, this if else can be used in loops also
            if j > N-1 or j < 0: return 0
            else: return Matrix[i][j]
        
        if N == 1: return max(Matrix[0])  # For Matrix 1 single row NO Path available as all moves are downwards
        
        # Starting from (N-2) row, as in the bottom most row (N-1) NO Path available 
        for i in range(N-2, -1, -1):
            for j in range(N-1, -1, -1):
                Matrix[i][j] += max(
                                    get(i+1, j),
                                    get(i+1, j-1),
                                    get(i+1, j+1)
                                    )
                                    
                res = max(res, Matrix[i][j])
        
    
        return res
            
# ------------------------------------------------ Method 2 --------------------------------------------------------------------------------

# Traversing from top-left most to bottom-right most corner
'''
We are adding max cost of previous path to the present path
Given Paths traversing patterns are: From Matrix[r][c] we can go to:
Matrix[r+1][c] 
Matrix[r+1][c-1]
Matrix[r+1][c+1]

At the current cell we want to find from what previous path we have come from so that
the cost would be maximum.
So from the Paths traversing patterns if we want to find the previous path traversing patterns 
the given patters will change to:
Matrix[r+1][c]   => Matrix[r-1][c]   => Matrix[i-1][c] 
Matrix[r+1][c-1] => Matrix[r-1][c+1] => Matrix[i-1][j+1]
Matrix[r+1][c+1] => Matrix[r-1][c-1] => Matrix[i-1][j-1]
'''
class Solution:
    def maximumPath(self, N, Matrix):
        
        mat = Matrix
        res = max(mat[0])  # if mat contains only 1 row
        
        for i in range(1, len(mat)):
            for j in range(len(mat[0])):
                
                if j > 0 and j < len(mat)-1: 
                    mat[i][j] += max(mat[i-1][j], mat[i-1][j+1], mat[i-1][j-1])
                    
                elif j == 0:
                    mat[i][j] += max(mat[i-1][j], mat[i-1][j+1])
                    
                elif j == len(mat)-1:
                    mat[i][j] += max(mat[i-1][j-1], mat[i-1][j])
                
                res = max(res, mat[i][j])
        
        return res
        
        
        
# Time Complexity: O(len(Matrix) * len(Matrix[0]))
# Space Complexity: O(1)  # we are not taking any new matrix only making changes in the given matrix.
