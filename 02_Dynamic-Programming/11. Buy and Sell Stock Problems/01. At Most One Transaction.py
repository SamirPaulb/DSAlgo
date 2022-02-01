# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices):
        minsofar = prices[0]
        maxprofit = 0

        for  i in range(len(prices)):
            minsofar = min(minsofar , prices[i])
            profit = prices[i] - minsofar 
            maxprofit = max(maxprofit, profit)
        
        return maxprofit

# Time: O(N)
# Space: O(1)