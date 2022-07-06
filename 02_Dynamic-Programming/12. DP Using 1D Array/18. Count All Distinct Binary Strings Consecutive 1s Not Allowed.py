# https://practice.geeksforgeeks.org/problems/consecutive-1s-not-allowed1912/1/#

class Solution:

	def countStrings(self,n):
	    if n == 1: return 2
    	dp = [0]*n
    	dp[0] = 2
    	dp[1] = 3
    	for i in range(2, n):
    	    dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1] % (10**9 + 7)

# Time: O(n)
# Space: O(n)
