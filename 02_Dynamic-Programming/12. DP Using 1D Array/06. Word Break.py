# https://leetcode.com/problems/word-break/
# https://youtu.be/Sx9NNgInc3A

# Memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(l, r):
            if l >= len(s): return True
            if r >= len(s): return False
            if (l,r) in dp: return dp[(l,r)]
            cur = s[l:r+1]
            if cur in wordDict:
                ans = dfs(r+1, r+1) or dfs(l, r+1)
            else:
                ans = dfs(l, r+1)
            dp[(l,r)] = ans
            return ans
        
        return dfs(0, 0)


# DP
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
        

        
        
# Time: O(N^2)
# Space: O(N)
