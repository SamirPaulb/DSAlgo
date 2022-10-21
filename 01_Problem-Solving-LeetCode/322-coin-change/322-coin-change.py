class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[2**31]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 0
        
        for j in range(1, amount+1):
            if j % coins[0] == 0:
                dp[1][j] = j // coins[0]
        
        for i in range(2, len(coins)+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    dp[i][j] = min(1 + dp[i][j - coins[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1] if dp[-1][-1] != 2**31 else -1