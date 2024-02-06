# https://www.lintcode.com/problem/787
# https://www.youtube.com/watch?v=mjDfgdGp-II


from typing import List
import collections

class Solution:
    def hasPath(self, maze, start, destination):
        q = collections.deque([start])
        row = len(maze)
        col = len(maze[0])
        while q:
            i, j = q.popleft()
            maze[i][j] = 2
            if i == destination[0] and j == destination[1]: return True
            for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
                x,y = i,j
                while 0 <= x+dx < row and 0 <= y+dy < col and maze[x+dx][y+dy] != 1:
                    x += dx
                    y += dy
                if maze[x][y] == 0: q.append([x, y])
        
        return False

# Time: O(row * col)
# Space: O(1)
