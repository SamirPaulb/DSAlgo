# https://www.youtube.com/watch?v=ntCGbPMeqgg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=6
# https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

# Memoization
class Solution:
    def knapSack(self,W, wt, val, n):
        dp = [[-1]*(W+1) for _ in range(n+1)]
        def dfs(n, W):
            if W == 0 or n == 0: return 0
            if dp[n][W] != -1: return dp[n][W]
            
            if wt[n-1] <= W:
                dp[n][W] = max(dfs(n-1, W), val[n-1] + dfs(n-1, W-wt[n-1]))
            else:
                dp[n][W] = dfs(n-1, W)
            return dp[n][W]
        
        return dfs(n, W)
    
    
# Dynamic Programming
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
        
