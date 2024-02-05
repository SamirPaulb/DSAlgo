# https://www.lintcode.com/problem/860
# https://www.youtube.com/watch?v=7zmgQSJghpo
# https://leetcode.com/problems/number-of-distinct-islands/

from typing import List,
import collections
class Solution:
    def numberof_distinct_islands(self, grid: List[List[int]]) -> int:
        direc = [(1,0),(-1,0),(0,1),(0,-1)]
        row, col = len(grid), len(grid[0])
        uniqueIsland = set()
        q = collections.deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    path = ""
                    q.append((i,j))
                    while q:
                        r,c = q.popleft()
                        grid[r][c] = 0
                        for dx,dy in direc:
                            nr,nc = r+dx, c+dy
                            if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                                path += str(nr-i) + str(nc-j)
                                q.append((nr,nc))
                    uniqueIsland.add(path)
        return len(uniqueIsland)
