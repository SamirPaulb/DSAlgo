# https://leetcode.com/problems/minimum-path-sum/

# --------------------- Method 1 ------------------------------------------------------------------------------

# https://www.youtube.com/watch?v=BzTIOsC0xWM
# Traversing from bottom-right most to top-left most corner
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid); c = len(grid[0])
        
        # in (c-1)th coloumn only 1 path available. ie, straight down. So bottom to up path along right most column is continuous sum of elements
        for i in range(r-2, -1, -1):
            grid[i][c-1] += grid[i+1][c-1]
        
        # in (r-1)th row only 1 path is available => straight right. so right to left path along bottom most row is contigeuos sum of elements
        for j in range(c-2, -1, -1):
            grid[r-1][j] += grid[r-1][j+1]
        
        # from (r-2, c-2) to (0, 0) path => in any cell add minimum value of down or right cell 
        for i in range(r-2, -1, -1):
            for j in range(c-2, -1, -1):
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
        
        return grid[0][0]
    


# --------------------- Method 2 ------------------------------------------------------------------------------

# Traversing from top-left most to bottom-right most corner
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
