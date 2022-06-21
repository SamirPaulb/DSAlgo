# https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1#

class Solution:
	def maxSumIS(self, arr, n):
		dp = arr.copy()  # dp = [i for i in arr]
		
		for i in range(n):
		    for j in range(i):
		        if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
		            dp[i] = dp[j] + arr[i]
        
        return max(dp)
		
		
# Time: O(n^2)
# Space: O(n)
		
