# https://www.lintcode.com/problem/788/
# https://algo.monster/liteproblems/505

from typing import List
import collections

class Solution:
    def shortest_distance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        distance = [[float('inf')]*col for _ in range(row)]
        distance[start[0]][start[1]] = 0

        q = collections.deque()
        q.append((start[0], start[1]))
        while q:
            i, j = q.popleft()
            for dx, dy in (1,0), (-1,0), (0,1), (0,-1):
                x, y, d = i, j, distance[i][j]
                while 0<=x+dx<row and 0<=y+dy<col and maze[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
                    d += 1
                if d < distance[x][y]:
                    distance[x][y] = d
                    q.append((x,y))
        print(distance)
        res = distance[destination[0]][destination[1]]
        return res if res != float('inf') else -1   

# Time: O(row * col * W)   # W is the maximum number of times a cell may be visited
# Space: O(row * col)
