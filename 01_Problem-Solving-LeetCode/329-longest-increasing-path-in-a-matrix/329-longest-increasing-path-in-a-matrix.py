class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        memo = {}
        move = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(i, j):
            if (i,j) in memo: return memo[(i,j)]
            ans = 1
            tmp = matrix[i][j]
            for m in move:
                r = i + m[0]
                c = j + m[1]
                if 0<=r<row and 0<=c<col and matrix[r][c] != '#' and matrix[r][c] > matrix[i][j]: 
                    matrix[i][j] = '#'
                    ans = max(ans, 1 + dfs(r,c))
                    matrix[i][j] = tmp
            memo[(i,j)] = ans
            return ans 
        
        res = 0
        for i in range(row):
            for j in range(col):
                res = max(res, dfs(i,j))
        return res