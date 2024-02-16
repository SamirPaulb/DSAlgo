# https://www.lintcode.com/problem/663

from typing import List
import collections

class Solution:
    def walls_and_gates(self, rooms: List[List[int]]):
        row, col = len(rooms), len(rooms[0])
        EMPTY, GATE = 2*31-1, 0
        q = collections.deque()
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == GATE:
                    q.append((i,j))
        while q:
            i,j = q.popleft()
            for dx,dy in (1,0), (-1,0), (0,1), (0,-1):
                x,y = i+dx, j+dy
                if 0<=x<row and 0<=y<col and rooms[i][j] + 1 < rooms[x][y]:
                    rooms[x][y] = rooms[i][j] + 1
                    q.append((x,y))

# Time: O(row * col)
# Space: O(cnt_GATE + cnt_EMPTY)
