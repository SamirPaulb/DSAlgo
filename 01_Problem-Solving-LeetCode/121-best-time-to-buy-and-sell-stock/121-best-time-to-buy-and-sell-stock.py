class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mini = prices[0]
        for i in prices:
            mini = min(i, mini)
            res = max(res, i-mini)
        return res