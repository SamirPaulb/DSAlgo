# https://leetcode.com/problems/rotate-image/
# https://www.youtube.com/watch?v=Y72QeX0Efxw
'''
First Transpose(flip matrix over its diagonal) the matrix then rotate every rows
[[1,2,3],                [[1,4,7],                 [[7,4,1],
 [4,5,6],  =>Transpose=>  [2,5,8], =>Rotate rows=>  [8,5,2],
 [7,8,9]]                 [3,6,9]]                  [9,6,3]]
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        #Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #Rotate rows
        for i in range(n):
            l, r = 0, n - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1; r -= 1
        return matrix

# Time Complexity = O(n*n)
# Space Complexity = O(1)