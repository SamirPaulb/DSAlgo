class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        mini = prices[0]
        tmpres = 0
        profit1 = [0]*n
        for i in range(n):
            mini = min(mini, prices[i])
            tmpres = max(tmpres, prices[i] - mini)
            profit1[i] = tmpres
        
        maxi = prices[n-1]
        tmpres = 0
        profit2 = [0]*n
        for i in range(n-1, -1, -1):
            maxi = max(maxi, prices[i])
            tmpres = max(tmpres, maxi - prices[i])
            profit2[i] = tmpres
        
        res = 0
        for i in range(n):
            res = max(res, profit1[i] + profit2[i])
        
        print(profit1)
        print(profit2)
        return res