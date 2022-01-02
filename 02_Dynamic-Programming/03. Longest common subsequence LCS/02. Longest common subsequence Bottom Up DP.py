'''  
https://www.youtube.com/watch?v=g_hIx4yn9zg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=20
https://leetcode.com/problems/longest-common-subsequence/
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        X = text1; Y = text2; m = len(text1); n = len(text2)
        dp = [[0] * (n+1) for i in range(m+1)]
        # Base case => m == 0 or n == 0 => NO common subsequence
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0: dp[i][j] = 0
        
        # Filling rest dp
        for i in range(1, m+1):
            for j in range(1, n+1):
                if X[i-1] == Y[j-1]: 
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return dp[-1][-1]
    
