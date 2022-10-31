# https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [[-2,-1], [-2,1], [2,-1], [2,1], [-1,-2], [-1,2], [1,-2], [1,2]]
        memo = {}
        def dfs(r, c, k):
            if k == 0: return 1
            if (r, c, k) in memo: return memo[(r,c,k)]
            tmp = 0
            for m in moves:
                i = r + m[0]; j = c + m[1]
                if 0 <= i < n and 0 <= j < n:
                    tmp += dfs(i, j, k-1)
            
            memo[r,c,k] = tmp / 8
            return memo[(r,c,k)]
        
        return dfs(row, column, k)
