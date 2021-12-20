# https://www.youtube.com/watch?v=ntCGbPMeqgg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=6
# https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp = [[0] * (W + 1) for i in range(n + 1)]
        for i in range(n + 1):
            for j in range(W + 1):
                if j == 0 or i == 0: dp[i][j] = 0
                elif wt[i - 1] <= j:
                    dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[-1][-1]
        