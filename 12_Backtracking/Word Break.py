# https://leetcode.com/problems/word-break/
# https://youtu.be/Sx9NNgInc3A

# Recursion
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.res = False
        def solve(s):
            if not s: 
                self.res = True
                return
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    solve(s[i:])
        
        solve(s)
        return self.res
# Time: O(N^2)
# Space: O(1)
        




# Dynamic Programming
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[n] = True
        
        for i in range(n-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= n and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                    if dp[i] == True: 
                        break
        
        return dp[0]

# Time: O(N^2)
# Space: O(N)
