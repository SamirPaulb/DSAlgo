# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        if n < 3: return min(cost)
        
        for i in range(2, n):
            cost[i] += min(cost[i-1], cost[i-2])
        
        return min(cost[-1], cost[-2])
    
# Time: O(N)
# Space: O(1); as we are using given array for DP