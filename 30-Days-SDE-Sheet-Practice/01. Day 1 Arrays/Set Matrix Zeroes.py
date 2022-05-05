# https://leetcode.com/problems/set-matrix-zeroes/
# Approach:
'''
Instead of taking two separate dummy arrays, 
take first row and column of the matrix as the array for 
checking whether the particular column or row has the value 0 or not. 
Since matrix[0][0] are overlapping. Therefore take separate variable col0(say) to check 
if the 0th column has 0 or not and use matrix[0][0] to check if the 0th row has 0 or not. 
Now traverse from last element to the first element and check if matrix[i][0]==0 || matrix[0][j]==0 
and if true set matrix[i][j]=0, else continue.
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col0 = 1
        
        for i in range(len(matrix)):
            # checking if 0 is present in the 0th column or not
            if matrix[i][0] == 0: 
                col0 = 0
            # starting j from 1 or-else it may change 0th row value
            for j in range(1, len(matrix[0])): 
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])-1, 0, -1):
                # traversing in the reverse direction and checking if the row or col has 0 or not and setting values of matrix accordingly.
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
                    
        return matrix

# Time: O(N * M)
# Space: O(1)