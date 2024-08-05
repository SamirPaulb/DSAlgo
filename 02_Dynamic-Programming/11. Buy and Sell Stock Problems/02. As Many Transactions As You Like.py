# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# https://www.youtube.com/watch?v=nGJmxkUJQGs

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def solve(i, can_sell):
            if i == len(prices): 
                return 0
            if (i, can_sell) in memo: 
                return memo[(i, can_sell)]
            if can_sell == 1:
                profit = max(prices[i] + solve(i+1, 0), solve(i+1, 1))
            else:
                profit = max(-prices[i] + solve(i+1, 1), solve(i+1, 0))
            memo[(i, can_sell)] = profit
            return profit
        return solve(0, 0)

# Time: O(2 * N)
# Space: O(N + N)

################################################################################################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]
        dp[0][0] = -2**31
        for i in range(1, n+1):
            for can_sell in range(2):
                if can_sell == 1:
                    dp[i][can_sell] = max(prices[i-1] + dp[i-1][0], dp[i-1][1])
                else:
                    dp[i][can_sell] = max(-prices[i-1] + dp[i-1][1], dp[i-1][0])
        return dp[-1][1]

################################################################################################

class Solution:
    def maxProfit(self, prices):
        res = 0

        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                res += prices[i+1] - prices[i]
        
        return res
