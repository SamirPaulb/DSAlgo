class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = []
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1: q.append((i,j))
        
        if len(q) == 0 or len(q) == n*n: return -1
        
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        res = -1
        while q:
            l = len(q)
            for i in range(l):
                cur = q.pop(0)
                for direc in directions:
                    r = cur[0] + direc[0]
                    c = cur[1] + direc[1]
                    if not 0 <= r < n or not 0 <= c < n or grid[r][c] == 1: continue
                    grid[r][c] = 1
                    q.append((r,c))
            res += 1
        
        return res