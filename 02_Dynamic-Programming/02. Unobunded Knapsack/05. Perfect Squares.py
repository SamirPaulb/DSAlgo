# https://leetcode.com/problems/perfect-squares/

'''
# Coin Change

class Solution:
    def numSquares(self, n: int) -> int:
        row = int(math.sqrt(n)) + 1
        dp = [[2**31]*(n+1) for i in range(row)]
        for i in range(row):
            dp[i][0] = 0
        for i in range(1, row):
            for j in range(1, n+1):
                if i**2 <= j:
                    dp[i][j] = min(dp[i-1][j], 1 + dp[i][j - i**2])
                else:
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        return dp[-1][-1]
        
# Time: O(N * N^1/2)
# Space: O(N * N^1/2)
'''


# 1D DP
# https://youtu.be/HLZLwjzIVGo

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for s in range(i):
                sq = s * s
                if sq > i: break
                if 1 + dp[i - sq] < dp[i]:
                    dp[i] = 1 + dp[i - sq]
        
        return dp[n]
    
# Time: O(N * N^1/2)
# Space: O(N)
