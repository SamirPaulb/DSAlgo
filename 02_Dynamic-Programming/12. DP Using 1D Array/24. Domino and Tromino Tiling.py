# https://leetcode.com/problems/domino-and-tromino-tiling/


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0, 1, 2, 5] + [1] * n
        if n <= 3: return dp[n]
        
        for i in range(4, n+1):
            dp[i] = ((2 * dp[i-1]) % MOD + dp[i-3])% MOD
        
        return dp[n]
      
# Time: O(N)
# Space: O(N)
