# https://www.youtube.com/watch?v=aycn9KO8_Ls&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=14
# https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1#

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        dp = [[0] * (W + 1) for i in range(N + 1)]
        
        # innitializing 0th row and 0th colomn = 0
        # as for zero weight profit will be zero and we are placing profit in each box
            
        for i in range(1, N + 1):
            for j in range(1, W + 1):
                if wt[i - 1] <= j:
                    dp[i][j] = max(val[i-1] + dp[i][j-wt[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]