# https://leetcode.com/problems/wildcard-matching/
# https://youtu.be/NbgUZAoIz3g

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

    
    
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(s) + 1) for _ in range(len(p) + 1)]
        
        for i in range(len(dp)-1, -1, -1):
            for j in range(len(dp[0])-1, -1, -1):
                if i == len(dp)-1 and j == len(dp[0])-1:
                    dp[i][j] = True
                elif i == len(dp)-1:
                    dp[i][j] = False
                elif j == len(dp[0])-1:
                    if p[i] == '*': dp[i][j] = dp[i+1][j]
                    else: dp[i][j] = False
                else:
                    if p[i] == "?":
                        dp[i][j] = dp[i+1][j+1]
                    elif p[i] == '*':
                        dp[i][j] = dp[i+1][j] or dp[i][j+1]
                    elif p[i] == s[j]:
                        dp[i][j] = dp[i+1][j+1]
                    else:
                        dp[i][j] = False
        
        return dp[0][0]

'''
