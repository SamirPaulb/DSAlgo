# https://youtu.be/3YILP-PdEJA
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# -------------------------------  Recursive + Memoization => TLE -----------------------------------
class Solution:
    def maxProfit(self, k, prices):
        # Same as Matrix Chain Multiplication
        n = len(prices) - 1
        dp = [[-1]*(n+1) for i in range(k+1)]
        
        def solve(k, n):
            if k == 0 or n < 1: return 0
            
            if dp[k][n] != -1: return dp[k][n]
            
            ans = -2**31 - 1
            for i in range(n):
                ans = max(ans, solve(k-1, i) + (prices[n] - prices[i])) # Max profit for (k-1) transactions and stocks before today
            
            ans =  max(ans, solve(k, n-1))
            
            dp[k][n] = ans
            return dp[k][n]
        
        return solve(k, n)

# Time Complexity: O(n^2 * k)
# Space Complexity: O(n*k)
# This solution will give TLE


# -------------------------------  Dynamic Programming => TLE ----------------------------------------
class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n <= 1 or k == 0: return 0
        
        dp = [[0]*n for t in range(k+1)]
        
        for t in range(1, k+1):    # transaction
            for d in range(1, n):  # day
                
                ans = -2**31 -1
                
                for p in range(d): # previous days where (t-1) transactions allowed
                    ans = max(ans, dp[t-1][p] + prices[d]- prices[p])
                    
                ans = max(ans, dp[t][d-1]) # previous day with t transactions allowed
                
                dp[t][d] = ans
        
        return dp[-1][-1]

# Time Complexity: O(n^2 * k)
# Space Complexity: O(n*k)
# This solution will give TLE


# -------------------------------  Dynamic Programming => OPTIMAL All TestCases Passed -----------------
class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n <= 1 or k== 0: return 0
        
        dp = [[0]*n for i in range(k+1)]
        
        for t in range(1, k+1):    # number transactions allowed
            prevMax = float("-inf")  # to store the max profit for (t-1) transactions on previous days 
            for d in range(1, n):  # current day
                prevMax = max(prevMax, dp[t-1][d-1] - prices[d-1])
                dp[t][d] = max(prevMax + prices[d], dp[t][d-1])
                
        return dp[-1][-1]
        
# Time Complexity: O(n*k)
# Space Complexity: O(n*k)


# -------------------------------  running Kadane's algo K times => Most OPTIMAL All TestCases Passed -----------------

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
    
        if not prices:
            return 0

        # for array of lenght n at most n//2 transactions posible. if k >= n//2 we can perform the method of best-time-to-buy-and-sell-stock-ii
        if k >= len(prices) // 2:   
            return sum(
                x - y
                for x, y in zip(prices[1:], prices[:-1])
                if x > y)
        
        
        profits = [0]*len(prices)
        for j in range(k):

            preprofit = 0
            for i in range(1,len(prices)):
            
                profit = prices[i] - prices[i-1]
                preprofit = max(preprofit+profit, profits[i])
                profits[i] = max(profits[i-1], preprofit)
    
        return profits[-1]
    
# Time Complexity: O(n*k)
# Space Complexity: O(n)
