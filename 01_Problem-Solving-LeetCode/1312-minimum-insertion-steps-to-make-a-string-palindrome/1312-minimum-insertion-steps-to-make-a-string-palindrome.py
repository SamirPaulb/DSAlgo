class Solution:
    def minInsertions(self, s: str) -> int:
        def lcs(x, y):
            dp = [[0]*(len(x)+1) for i in range(len(y)+1)]
            for i in range(1, len(x)+1):
                for j in range(1, len(y)+1):   
                    if x[i-1] == y[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
            return dp[-1][-1]
        
        return len(s) - lcs(s, s[::-1])
    