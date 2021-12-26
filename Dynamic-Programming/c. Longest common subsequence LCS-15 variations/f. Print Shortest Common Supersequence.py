# https://www.youtube.com/watch?v=VDhRg-ZJTuc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=29
# https://leetcode.com/problems/shortest-common-supersequence/

'''
Using Printing Longest Common Subsequence(LCS)
The Path of printing LCS in dp matrix is the Common Supersequence
which contains both strings X and Y
'''
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        X = str1; Y = str2; m = len(X); n = len(Y)
        dp = [[0]*(n+1) for i in range(m+1)]
        # As now finding LCS dp
        # 0th column and 0th row of dp = 0 as with any of X or Y of length 0; NO common subsequence possible
        for i in range(1, m+1):
            for j in range(1, n+1):
                if X[i-1] == Y[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        # Now traverse from (m, m) to (0, 0) and store the path in res
        # this path is actually Common Supersequence
        i = m; j = n; res = ""
        while i > 0 and j > 0:
            if X[i-1] == Y[j-1]:
                res += X[i-1]    # or Y[j-1] same
                i -= 1; j -= 1
            else:
                if dp[i][j-1] > dp[i-1][j]:
                    res += Y[j-1] # add Y[j-1] as this greater
                    j -= 1
                else:
                    res += X[i-1]
                    i -= 1
        
        # If any of i == 0 or j == 0; then also we have to add the remaining elelments as Supersequence containd all common elelments of X and Y
        while i > 0:
            res += X[i-1]
            i -= 1
        
        while j > 0:
            res += Y[j-1]
            j -= 1
        
        return res[::-1]  # reverse of res as we have traversed from the end
    
                