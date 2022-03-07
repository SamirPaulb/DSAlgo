# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid); n = len(grid[0])
        res = 0
        
        def dfs(i, j):
            if (not 0 <= i < m) or (not 0 <= j < n) or (grid[i][j] == "0"): return
            grid[i][j] = "0"
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0": continue
                dfs(i, j)
                res += 1
        
        return res
        