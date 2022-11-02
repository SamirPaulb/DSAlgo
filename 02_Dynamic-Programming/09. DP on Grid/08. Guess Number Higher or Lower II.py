# https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# https://youtu.be/x--bMzT1Xhk

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[-1]*(n+1) for _ in range(n+1)]
        @lru_cache(None)
        
        def solve(start, end):
            if start >= end: return 0
            ans = 2**31
            if dp[start][end] != -1: return dp[start][end]
            for i in range(start, end):
                ans = min(ans, i + max(solve(start, i-1), solve(i+1, end)))
            dp[start][end] = ans
            return ans
        # print(dp)
        return solve(1, n)
      
        
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[2**31]*(n+1) for _ in range(n+1)]
        
        for i in range(n, 0, -1):
            for j in range(i, n+1):
                if i == j:
                    dp[i][j] = 0
                if j - i == 1: 
                    dp[i][j] = i
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], k + max(dp[i][k-1], dp[k+1][j]))
        # print(dp)
        return dp[1][-1]
    
    
    
# Time: O(N * N * N)
# Space: O(N * N)
