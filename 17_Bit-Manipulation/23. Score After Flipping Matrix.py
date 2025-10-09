https://leetcode.com/problems/score-after-flipping-matrix/description/

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            if grid[i][0] == 0:
                for j in range(col):
                    grid[i][j] = 1 - grid[i][j]
        
        colCnt1 = [0]*col
        for j in range(col):
            for i in range(row):
                if grid[i][j] == 1:
                    colCnt1[j] += 1
        
        for j in range(col):
            if colCnt1[j] < row / 2: 
                for i in range(row):
                    grid[i][j] = 1 - grid[i][j]
        
        res = 0
        for i in range(row):
            num = 0
            for j in range(col):
                num += grid[i][j] * (2**(col-j-1))
            res += num

        return res
