# https://www.youtube.com/watch?v=9uUVFNOT3_Y&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=34
# https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1#

import sys  
class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        dp = [[-1]*101 for i in range(501)]
        # bottom up manner Memoization 
        def solve(arr, i, j):
            if i >= j: return 0
            if dp[i][j] != -1: # this subproblem had already calculated so don't need to calculate again, return the the stored value
                return dp[i][j]
            ans = sys.maxsize
            for k in range(i, j):
                temp = solve(arr, i, k) + solve(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
                ans = min(ans, temp)
            #recomputations of same subproblems can be avoided by storing the temp value in dp[i][j] in bottom up manner.
            dp[i][j] = ans
            return dp[i][j]
        
        return solve(arr, 1, len(arr)-1)

    