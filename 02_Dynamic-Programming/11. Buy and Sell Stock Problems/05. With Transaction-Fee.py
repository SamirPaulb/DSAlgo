# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        obsp = - prices[0]   # Old Brought State Profite
        ossp = 0             # Old Sold State Profite
        
        for i in range(1, len(prices)):
            nbsp = 0         # New Brought State Profit
            nssp = 0         # New Sold State Profit
            
            nbsp = max(ossp - prices[i], obsp)
            nssp = max(obsp + prices[i] - fee, ossp)
            
            obsp = nbsp
            ossp = nssp
        
        return ossp

# Time: O(n)
# Space: O(1)