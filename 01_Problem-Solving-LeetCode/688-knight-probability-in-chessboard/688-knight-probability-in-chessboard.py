class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        move = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]] 
        memo = {}
        def solve(r, c, k):
            if not 0 <= r < n or not 0 <= c < n: return 0
            if k == 0: return 1
            key = (r, c, k)
            if key in memo:
                return memo[key]
            tmp = 0
            for m in move:
                i = r + m[0]
                j = c + m[1]
                tmp += solve(i,  j, k-1)
            memo[key] = tmp / 8
            return memo[key]
        
        return solve(row, column, k)