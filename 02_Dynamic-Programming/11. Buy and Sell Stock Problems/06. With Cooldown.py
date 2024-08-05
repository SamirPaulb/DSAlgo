# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def solve(i, can_sell):
            if i >= len(prices): return 0
            if (i,can_sell) in memo: return memo[(i,can_sell)]
            if can_sell == 1: 
                profit = max(prices[i] + solve(i+2,0), solve(i+1,1))    # After selling cooldown one day
            else:
                profit = max(-prices[i] + solve(i+1,1), solve(i+1,0))
            memo[(i,can_sell)] = profit
            return profit
        return solve(0,0)
    
# Time: O(2 * N)
# Space: O(2 * N)
