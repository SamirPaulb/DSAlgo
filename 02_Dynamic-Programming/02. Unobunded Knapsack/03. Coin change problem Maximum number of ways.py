# https://www.youtube.com/watch?v=I4UR2T6Ro3w&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=16&t=299s
# https://practice.geeksforgeeks.org/problems/coin-change2448/1#
# https://leetcode.com/problems/coin-change-2/

class Solution:
    def count(self, S, m, n): # array S[] its size m and n as input parameter 
        # code here 
        dp = [[0]*(n + 1) for i in range(m+1)]
        # dp[0][0] = 0; as for S of size 0 no possible coins change
        # in 1st row for array os size zero no posible combination so 0
        # in 1st column i from 1 <= i <= m, dp[i][0] = 1 as for any size greater than equal to 1 null or empty subset ie. coin change possile
        
        for i in range(1, m + 1):
            dp[i][0] = 1
        
        for i in range(1, m +1):
            for j in range(1, n+1):
                if S[i-1] <= j:
                    dp[i][j] = dp[i][j - S[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
        