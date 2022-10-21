class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid); n = len(grid[0])
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        
        def makeWater(i, j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] == "0": return
            grid[i][j] = "0"
            makeWater(i+1, j)
            makeWater(i-1, j)
            makeWater(i, j+1)
            makeWater(i, j-1)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    makeWater(i, j)
                    res += 1
                    
        return res