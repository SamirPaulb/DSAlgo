# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def dfs(s):
            if s and s[0] == "0": return 0
            if not s or len(s) == 1: return 1
            if s in memo: return memo[s]
            if int(s[:2]) <= 26: ans = dfs(s[1:]) + dfs(s[2:])
            else: ans = dfs(s[1:])
            memo[s] = ans
            return memo[s]
          
        return dfs(s)
        
# Time: O(N)
# Space: O(N)
            
  
  
 class Solution:  
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if s[i] != '0':  # Single digit
                dp[i] = dp[i+1]
            if i+1 < n and (s[i] == '1' or s[i] == '2' and s[i+1] <= '6'):  # Two digits
                dp[i] += dp[i+2]
        return dp[0]
      
# Time: O(N), where N <= 100 is length of string s.
# Space: O(N)
      
