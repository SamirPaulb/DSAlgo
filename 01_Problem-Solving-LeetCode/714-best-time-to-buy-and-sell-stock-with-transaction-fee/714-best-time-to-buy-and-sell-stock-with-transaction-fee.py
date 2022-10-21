class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        obsp = -prices[0]
        ossp = 0
        
        for price in prices[1:]:
            nbsp = 0
            nssp = 0
            
            nbsp = max(ossp - price, obsp)
            nssp = max(obsp + price - fee, ossp)
            
            obsp = nbsp
            ossp = nssp
        
        return ossp