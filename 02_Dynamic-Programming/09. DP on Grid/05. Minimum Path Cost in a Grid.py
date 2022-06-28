# https://leetcode.com/problems/minimum-path-cost-in-a-grid/

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        '''
        NOTE: Incase of matrix (2-D Array) Python's matrix.copy() function Does NOT make a new copy of original matrix. So any change in new_matrix will cange in original matrix.
        '''
        dp = self.deepcopy(grid)  # Can NOT use, dp = grid.copy()  or  dp = grid[:]
        
        for i in range(1, row):
            for j in range(col):
                val = 2**31
                for k in range(col):
                    val = min(val, dp[i-1][k] + moveCost[grid[i-1][k]][j])
                dp[i][j] += val
        
        return min(dp[-1])
    
    def deepcopy(self, arr):
        n = len(arr)
        m = len(arr[0])
        new_arr = [[0]*m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                new_arr[i][j] = arr[i][j]
        
        return new_arr

    


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

