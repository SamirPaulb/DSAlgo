# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        row = len(coins); col = amount + 1
        dp = [[2**31]*col for i in range(row)]
        
        for j in range(col):
            if j % coins[0] == 0:
                dp[0][j] = j // coins[0]
        
        for i in range(row):
            dp[i][0] = 0
        
        for i in range(1, row):
            for j in range(1, col):
                if j < coins[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(1 + dp[i][j - coins[i]], dp[i-1][j])
        
        res = dp[-1][-1]
        return res if res != 2**31 else -1

        