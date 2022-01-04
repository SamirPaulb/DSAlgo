# https://www.youtube.com/watch?v=BzTIOsC0xWM
# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # get dimensions
        n = len(grid) # no of cells in each col
        m = len(grid[0]) # no of cells in each row
        
        # populate first row using m for no of cells in row
        for i in range(1,m):
            grid[0][i] = grid[0][i] + grid[0][i-1]
        
        # populate first col using n for no of cells in col
        for j in range(1,n):
            grid[j][0] = grid[j-1][0] + grid[j][0]
        
        # populate the rest
        for i in range(1,n):
            for j in range(1,m):
				# get min seen so far plus curr cell value
                grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
        
        # return last cell
        return grid[-1][-1]


# Time: O(m*n)
# Space: O(1)
