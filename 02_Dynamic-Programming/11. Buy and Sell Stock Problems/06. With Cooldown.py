# https://youtu.be/GY0O57llkKQ
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices):
        obsp = - prices[0]  # Old Brought State Profit
        ossp = 0            # Old Sold State Profit
        ocsp = 0            # Old Cold State Profit
        
        for i in range(1, len(prices)):
            nbsp = 0        # New Brought State Profit
            nssp = 0        # New Sold State Profit
            ncsp = 0        # New Cold State Profit
            
            nbsp = max(ocsp - prices[i], obsp)
            nssp = max(obsp + prices[i], ossp)
            ncsp = max(ossp, ocsp)
            
            obsp = nbsp
            ossp = nssp
            ocsp = ncsp
        
        return ossp