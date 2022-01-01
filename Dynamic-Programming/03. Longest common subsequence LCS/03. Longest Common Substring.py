# https://www.youtube.com/watch?v=HrybPYpOvz0&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=22
# https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1#

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        dp = [[0]*(m+1) for i in range(n+1)]
        res = 0
        # as after a discontinuity we are again asigning dp[i][j] = 0; sd to store max length of Common substring.
        for i in range(1, n+1):
            for j in range(1, m+1):
                if S1[i-1] == S2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return res