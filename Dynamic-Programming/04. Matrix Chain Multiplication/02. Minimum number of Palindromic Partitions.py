# https://www.youtube.com/watch?v=fOUlNlawdAU&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=36
# https://www.youtube.com/watch?v=9h10fqkI7Nk&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=37
# https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1#

import sys
class Solution:
    def palindromicPartition(self, string):
        # code here
        s = string; i = 0; j = len(s) - 1
        dp = [[-1]*502 for i in range(502)]
        def solve(s, i, j):
            if i >= j: return 0
            if self.isPalindrome(s, i, j): return 0
            if dp[i][j] != -1: return dp[i][j]
            ans = sys.maxsize    # max size of integer in python
            for k in range(i, j):
                # temp = 1 + solve(s, i, k) + solve(s, k+1, j)
                # before calling solve(s, i, k) and solve(s, k+1, j)
                # Checking whether they are calculated previously or not
                # if calculated previously thenn don't need to calculate again
                # Optimizeation of solve(s, i, k)
                if dp[i][k] != -1:  # solve(s, i, k) was calculated previously and stored in dp[i][k]
                    left = dp[i][k] # don't need to calculate aagin return stored vslue
                else:  # solve(s, i, k) was not calculated previously; so we need to calculate now
                    left = solve(s, i, k)
                    dp[i][k] = left    # storing left value in dp[i][k] for future use
                # Optimization for solve(s, k+1, j)
                if dp[k+1][j] != -1:   # solve(s, k+1, j) was calculated previously and stored in dp[k+1][j]
                    right = dp[k+1][j] # don't need to calculate aagin return stored vslue
                else:  # solve(s, k+1, j) was not calculated previously; so we need to calculate now
                    right = solve(s, k+1, j)
                    dp[k+1][j] = right # storing left value in dp[k+1][j] for future use
                
                # Now calculate temp
                temp = 1 + left + right
                ans = min(ans, temp)
                
            dp[i][j] = ans
            return dp[i][j]
        
        return solve(s, i, j)
        
    def isPalindrome(self, s, i, j):
        return s[i:j+1] == s[i:j+1][::-1]



