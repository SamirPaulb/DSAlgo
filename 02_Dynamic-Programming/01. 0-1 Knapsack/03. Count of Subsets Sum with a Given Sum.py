# https://www.youtube.com/watch?v=F7wqWbqYn9g&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=11
# https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1#
# https://leetcode.com/problems/

class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
		dp = [[0] * (sum + 1) for i in range(n + 1)]
		# Changing 1st row = 0 as size of arr is 0 so not given sum > 0 is possible
		for j in range(sum + 1):
		    dp[0][j] = 0
		# changing 1st column = 1 as sum = 0 is posible for every empty subset
		for i in range(n + 1):
		    dp[i][0] = 1
		# changing remaining dp
		for i in range(1, n + 1):
		    for j in range(1, sum + 1):
		        if arr[i - 1] <= j:
		            dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
		        else:
		            dp[i][j] = dp[i-1][j]

        return dp[n][sum]
        

	
	
	
	
'''
Given an array arr[] of integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.
Input: arr[] = {2, 3, 5, 6, 8, 10}
       sum = 10
Output: 3
Explanation: {2, 3, 5}, {2, 8}, {10}

'''
