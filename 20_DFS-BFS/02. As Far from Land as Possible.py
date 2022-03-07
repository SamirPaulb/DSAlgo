# https://leetcode.com/problems/as-far-from-land-as-possible/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # using concepts of 200. Number of Islands problem
        q = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append([i,j])
        
        # len(q) == 0  => All elements are 0 
        # len(q) == len(grid)*len(grid)  => All elements are 1
        if len(q) == 0 or len(q) == len(grid)*len(grid): return -1  # no land or water exists in the grid
        
        res = -1
        
        direction = [[1,0], [-1,0], [0,1], [0,-1]]
        
        while q: 
            for i in range(len(q)):
                curr = q.pop(0)  # as quequ so first in first out
                for direc in direction:
                    r = curr[0] + direc[0]
                    c = curr[1] + direc[1]
                    
                    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 1:
                        continue
                    q.append([r,c])
                    grid[r][c] = 1  # to mark this cell as visited
            # after making the q empty we forward 1 step in any direction where 0 is present. 
            res += 1
        
        # As we also added +1 to res for 1st time emptying queue but that cells with 1 was not in path so we started res = -1
        return res

        