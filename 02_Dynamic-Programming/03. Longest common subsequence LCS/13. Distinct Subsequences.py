# https://leetcode.com/problems/distinct-subsequences/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s)+1) for _ in range(len(t)+1)]
        
        # 0th row => len(t) == 0 and len(s) can be anything. So empty string t can be Subsequence of s
        for j in range(len(s)+1):
            dp[0][j] = 1
        
        for i in range(1, len(t)+1):
            for j in range(1, len(s)+1):
                dp[i][j] += dp[i][j-1]  # skip the current character s[j-1]
                if t[i-1] == s[j-1]:
                    dp[i][j] += dp[i-1][j-1]  # current character s[j-1] is used
        
        return dp[-1][-1]
    
    
# Time: O(n * m)
# Space: O(n * m)
