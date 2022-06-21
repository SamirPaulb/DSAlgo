# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        n = len(w1); m = len(w2)
        
        dp = [[0]*(m+1) for i in range(n+1)]
        
        for j in range(m+1): # Base Case 0th row where len(w1) = 0
            dp[0][j] = j
        
        for i in range(n+1): # Base Case 0th column where len(w2) = 0
            dp[i][0] = i
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if w1[i-1] == w2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                                        dp[i-1][j-1],  # Replace 
                                        dp[i-1][j],    # Delete
                                        dp[i][j-1]     # Insert
                                        )
        
        return dp[-1][-1]