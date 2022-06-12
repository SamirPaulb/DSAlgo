# https://leetcode.com/problems/minimum-path-cost-in-a-grid/

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[0]*col for i in range(row)]
        
        for j in range(col):
            dp[0][j] = grid[0][j]
        
        for i in range(1, row):
            for j in range(col):
                cost = [0]*col
                for k in range(col):
                    cost[k] = grid[i][j] + moveCost[grid[i-1][k]][j] + dp[i-1][k]
                dp[i][j] = min(cost)
        
        return min(dp[-1])
    
    
# Time: O(row * col * col)
# Space: O(row * col)

