# https://leetcode.com/problems/number-of-islands/

# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid); col = len(grid[0])
        res = 0
        
        def dfs(r, c):  # make surrounded '1' to '0'
            if ( not 0 <= r < row) or (not 0 <= c < col) or (grid[r][c] == '0'): return
            grid[r][c] = '0'
            dfs(i-1, j)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        
        return res
    
    
# BFS
import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid); col = len(grid[0])
        res = 0
        
        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            while q:
                r, c = q.popleft()
                if ( not 0 <= r < row) or (not 0 <= c < col) or (grid[r][c] == '0'): continue
                grid[r][c] = '0'
                q.append((r-1, c))
                q.append((r+1, c))
                q.append((r, c-1))
                q.append((r, c+1))
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res += 1
                    bfs(i, j)
        
        return res
    

# Time for both dfs and bfs is = number of nodes + number of edges
# Time: O(n + e)
# Space: O(n) + o(n)  
# Auxiliary Space: O(n)