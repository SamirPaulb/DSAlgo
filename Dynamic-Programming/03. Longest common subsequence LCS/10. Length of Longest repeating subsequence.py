# https://www.youtube.com/watch?v=hbTaCmQGqLg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=29
# https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1
'''
This problem is just the modification of Longest Common Subsequence problem. 
The idea is to find the LCS(str, str), where str is the input string with the restriction that
when both the characters are same, they shouldn’t be on the same index in the two strings(i != j).
'''
class Solution:
	def LongestRepeatingSubsequence(self, str):
	    X = str; Y = str; n = m = len(str)
		dp = [[0]*(n+1) for i in range(m+1)]
		# 0th row and 0th colomn initialize as 0; as for any of X or Y of length 0; NO common Subsequence possible
		# so start traversing dp matrix from (1, 1) to (n, m)
		for i in range(1, m+1):
		    for j in range(1, n+1):
		        if X[i-1] == Y[j-1] and i != j: # this is the only extra condition
		            dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return dp[-1][-1]
        
        