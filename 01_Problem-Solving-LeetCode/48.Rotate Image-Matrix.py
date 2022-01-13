# https://www.youtube.com/watch?v=Y72QeX0Efxw
'''
First Transpose(flip matrix over its diagonal) the matrix then rotate every rows
[[1,2,3],                [[1,4,7],                 [[7,4,1],
 [4,5,6],  =>Transpose=>  [2,5,8], =>Rotate rows=>  [8,5,2],
 [7,8,9]]                 [3,6,9]]                  [9,6,3]]
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #Transpose
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #Rotate rows
        for i in range(len(matrix)):
            l, r = 0, len(matrix[0]) - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1; r -= 1
        
        return matrix

# Time Complexity = O(N*N)
# Space Complexity = O(1)
            
        
        
        