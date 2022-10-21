class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        obsp = - prices[0]
        ossp = 0
        ocsp = 0
        
        for i in range(len(prices)):
            nbsp = 0
            nssp = 0
            ncsp = 0
            
            nbsp = max(ocsp - prices[i], obsp)
            nssp = max(obsp + prices[i], ossp)
            ncsp = max(ocsp, ossp)
            
            obsp = nbsp
            ossp = nssp
            ocsp = ncsp
        
        return ossp