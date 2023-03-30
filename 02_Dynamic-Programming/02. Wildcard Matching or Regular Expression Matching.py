# https://leetcode.com/problems/wildcard-matching/
# https://leetcode.com/problems/regular-expression-matching/
# https://youtu.be/NbgUZAoIz3g

# 44. Wildcard Matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        
        for i in range(len(s)+1):
            for j in range(len(p)+1):
                if i == j == 0: dp[i][j] = True
                elif j == 0: dp[i][j] = False
                elif i == 0:
                    if p[j-1] == '*': dp[i][j] = dp[i][j-1]
                    else: dp[i][j] = False 
                else:
                    if p[j-1] == '?': dp[i][j] = dp[i-1][j-1]
                    elif p[j-1] == '*': dp[i][j] = dp[i-1][j] or dp[i][j-1] 
                    elif s[i-1] == p[j-1]: dp[i][j] = dp[i-1][j-1]
                    else: dp[i][j] = False
        # print(dp)
        return dp[-1][-1]
