# https://leetcode.com/problems/longest-common-subsequence/

'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {} 
        
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if (i,j) in memo: return memo[(i,j)]
            
            elif text1[i] == text2[j]:
                ans = 1 + dfs(i+1, j+1)
            else:
                ans = max(dfs(i+1, j), dfs(i, j+1))
                
            memo[(i,j)] = ans
            return ans
        
        return dfs(0, 0)
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        x = text1; y = text2
        dp = [[0]*(len(y)+1) for i in range(len(x)+1)]
        
        for i in range(1, len(x)+1):
            for j in range(1, len(y)+1):
                if x[i-1] == y[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]