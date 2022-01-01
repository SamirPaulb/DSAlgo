# https://www.youtube.com/watch?v=-fx6aDxcWyg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=25
# https://practice.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1
# https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution:
	def minOperations(self, s1, s2):
		X = s1; Y = s2; m = len(X); n = len(Y)
		# Implement Longest Common Subsequence DP
		# LCS of X and Y is ea [X = "heap", Y = "pea"]
		# in X LCS will remain intact and remaining charecters will be removed
		# in LCS add the charecters present in Y
		dp = [[0] * (n+1) for i in range(m+1)]
		# in 0th row and 0th column No common subsecuence can be so 0
		for i in range(1, m+1):
		    for j in range(1, n+1):
		        if X[i-1] == Y[j-1]:
		            dp[i][j] = 1 + dp[i-1][j-1]
		        else:
		            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        lenOfLCS = dp[-1][-1]
        deletion = len(X) - lenOfLCS
        insertion = len(Y) - lenOfLCS
        
        return deletion + insertion
		
        