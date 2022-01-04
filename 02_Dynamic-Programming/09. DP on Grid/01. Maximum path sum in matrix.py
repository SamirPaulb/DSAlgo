# https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1#
'''
We are adding max cost of previous path to the present path
Given Paths traversing paterns are:
Matrix[r+1][c] 
Matrix[r+1][c-1]
Matrix[r+1][c+1]

At the current cell we want to find from what previous path we have come from so that
the cost would be maximum.
So from the Paths traversing paterns if we want to find the previous pathtraversing paterns 
the patters will change to:
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

