# https://leetcode.com/problems/search-a-2d-matrix/

'''Approach:
First use binary search to find the row in which the target is present.
Then apply binary search to the target row to check whether target present in targetRow or not.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find target row
        t = 0               # top row pointer
        b = len(matrix) - 1 # bottom row pointer
        while t <= b:
            mid = (t + b) // 2
            if target < matrix[mid][0]:
                b = mid - 1
            elif target > matrix[mid][-1]:
                t = mid + 1
            else:
                break
                
        # Now mid if the target row
        targetRow = mid
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[targetRow][mid]:
                r = mid - 1
            elif target > matrix[targetRow][mid]:
                l = mid + 1
            else:
                return True
        
        return False
    
# Time: O(log(n) + log(m)) = O(log(m*n)) 
# Space: O(1)