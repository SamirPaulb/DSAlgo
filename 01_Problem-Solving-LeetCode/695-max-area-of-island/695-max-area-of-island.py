class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        
        def dfs(i, j):
            if (not 0<=i<m) or (not 0<=j<n) or grid[i][j] == 0: return 0
            grid[i][j] = 0
            tmp = (dfs(i+1, j) +
                   dfs(i-1, j) +
                   dfs(i, j+1) +
                   dfs(i, j-1)) 
            return tmp + 1  # add 1 for the current grid[i][j] == 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        
        return res