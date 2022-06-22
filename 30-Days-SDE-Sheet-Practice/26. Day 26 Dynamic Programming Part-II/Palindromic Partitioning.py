# https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1#


class Solution:
    def palindromicPartition(self, string):
        # code here
        n = len(string) + 1
        dp = [[-1]*n for i in range(n)]
        
        def solve(s, i, j):
            if i >= j: return 0
            
            if s[i:j+1] == s[i:j+1][::-1] : return 0
            
            if dp[i][j] != -1: return dp[i][j]
            
            ans = 2**31
            for k in range(i, j):
                if dp[i][k] != -1:
                    left = dp[i][k]
                else:
                    left = solve(s, i, k)
                
                if dp[k+1][j] != -1:
                    right = dp[k+1][j]
                else:
                    right = solve(s, k+1, j)
                
                ans = min(ans, 1 + left + right)
                
            dp[i][j] = ans
            return dp[i][j]
        
        return solve(string, 0, n-1)
        
        
        