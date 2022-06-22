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
            for i in range(len(s)):
                if s[:i+1] in wordDict:
                    solve(s[i+1:])
                    
        solve(s)
        return self.res



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        
        for i in range(n-1, -1, -1):
            for word in wordDict:
                if i+len(word) <= n and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                    if dp[i] == True:
                        break
        
        return dp[0]
# Time: O(n * m)
# Space: O(n)

        
# Bottom-Up
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        
        for i in range(1, n+1):
            for j in range(i):
                if s[j:i] in wordDict:
                    dp[i] = dp[j]
                    if dp[i] == True: 
                        break
        
        return dp[-1]
        
# Time: O(n^2)
# Space: O(n)