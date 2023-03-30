# https://leetcode.com/problems/regular-expression-matching/
# https://youtu.be/HAA8mgxlov8

# Method 1 : Memoization / Top down ----------------------------------------

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        
        def dfs(i, j):
            if i >= len(s) and j >= len(p): 
                return True
            if j >= len(p): 
                return False
            if (i,j) in cache:
                return cache[(i,j)]
            match = i < len(s) and (s[i] == p[j] or p[j] == '.') 
            
            if j+1 < len(p) and p[j+1] == '*':
                ans = (dfs(i, j+2) or            # Not using *
                        (match and dfs(i+1, j)))  # Using *
            elif match:
                ans = dfs(i+1, j+1)
            else: 
                ans = False
            cache[(i,j)]= ans
            return ans
        
        return dfs(0,0)



# Method 2 : DP / Bottom up ----------------------------------------

class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]
