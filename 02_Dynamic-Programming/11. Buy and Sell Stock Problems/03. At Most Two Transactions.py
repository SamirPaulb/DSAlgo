# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Devide the array prices in two parts and apply buy and sell stock 1 approach on both part
        # But that would take O(n*n)
        # Trick:
        # make two new array. One to store the first part and other the second part
        # Add both elements of the 2 array of same indexed
        # Make Firt array by forward traversal of Prices
        # Make Second array by Reversed traversal of Prices
        
        n = len(prices)
        profit1, profit2 = [0] * n, [0] * n 

        # Forward Traversal For Storing The Profit of Left Part
        minSoFar = prices[0]
        maxProfitSoFar = 0
        for i in range(n):
        	maxProfitSoFar = max(maxProfitSoFar, prices[i] - minSoFar)
        	minSoFar = min(minSoFar, prices[i])
        	profit1[i] = maxProfitSoFar

        # Reversed Traversal For Storing The Profit of Right Part
        maxSoFar = prices[-1]
        maxProfitSoFar = 0
        for i in range(n - 1, -1, -1):
        	maxProfitSoFar = max(maxProfitSoFar, maxSoFar - prices[i])
        	maxSoFar = max(maxSoFar, prices[i])
        	profit2[i] = maxProfitSoFar

        # Add Profits of Left and Right Part
        res = 0
        for i in range(n):
        	res = max(res, profit1[i] + profit2[i])

        return res
    
        
# Time Complexity = O(n)
# Space Complexity = O(n)