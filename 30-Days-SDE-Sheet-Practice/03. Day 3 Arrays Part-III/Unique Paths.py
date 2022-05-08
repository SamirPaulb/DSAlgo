# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        def solve(m, n):
            if m == 1 or n == 1: return 1
            return solve(m, n-1) + solve(m-1, n)
        
        return solve(m, n)
        '''
        # converting above recursive solution into DP
        # filling with 1 so we don't need to write loops for base case
        dp = [[1]*(n+1) for i in range(m+1)] 
        
        # as for m == 1 or n == 1 path is 1 so starting from (2,2)
        for i in range(2, m+1):
            for j in range(2, n+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[-1][-1]   # last cell contains all paths  