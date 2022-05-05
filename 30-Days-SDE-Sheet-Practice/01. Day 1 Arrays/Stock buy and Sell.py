# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = prices[0]
        res = 0
        
        for price in prices:
            curMin = min(curMin, price)
            res = max(res, price - curMin)
        
        return res