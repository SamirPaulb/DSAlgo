# https://www.youtube.com/watch?v=I-l6PBeERuc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=16
# https://leetcode.com/problems/coin-change/

import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # As we have infinite supply of coins so this question is a variation of Unbounded Knapsack
        dp = [[sys.maxsize] * (amount + 1) for i in range(len(coins) + 1)] # placing max value as we want to find minimum
        # in Python 3 as sys.maxsize is max value of integer
        
        # Initializing 0th row = infinite = float("inf"); as for array coins of size zero it will take infinite coins to make amount j
        for j in range(amount + 1):
            dp[0][j] = sys.maxsize
        
        # Initializing 0th column from dp[1][0] to dp[len(coins)][0]  as 0
        # as for array coins of size >= 1; to make amount 0 don't need to take any coin so dp[i][0] = 0 for 1 <= i <= len(coins)
        for i in range(1, len(coins)+1):
            dp[i][0] = 0
        
# *** IN THIS QUESTION WE HAVE TO INITIALIZE 1st ROW ALSO ***
        # in 1st row check if amount j is multiple of coins[0] or not 
        # if multiple put number of coins[0] required to make amount j in dp[1][j]
        for j in range(1, amount + 1): 
            if j % coins[0] == 0:         # multiple or not
                dp[1][j] = j // coins[0]  # number of coins[0] required to make amount j
        
        # change remaing dp
        for i in range(2, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = min(1 + dp[i][j - coins[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        
        ans = dp[-1][-1] 
        return ans if ans != sys.maxsize else -1
                
                
# Time Complexity = O((len(coins)+1) * (amount+1))
# Space Complexity = O((len(coins)+1) * (amount+1))