# https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1, grid2):
        m = len(grid1) 
        n = len(grid1[0])
        
        def dfs(i, j):
            if not 0<=i<m or not 0<=j<n or grid2[i][j] == 0: return 
            grid2[i][j] = 0
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                dfs(i+dx, j+dy)
                
        # removing all the non-common sub-islands
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)
        
        res = 0
        # counting sub-islands
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1: 
                    dfs(i, j)
                    res += 1
        
        return res
                
        
# Time: O(m * n)
# Space: O(m * n) # Auxiliary Space
