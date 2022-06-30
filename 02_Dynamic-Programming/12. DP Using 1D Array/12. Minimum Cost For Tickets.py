# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        given_days = set(days)
        n = max(days) + 1
        dp = [0] * n
        
        for i in range(1, n):
            if i in given_days:
                if i >= 30: 
                    dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1], dp[i-30] + costs[2])
                elif 7 <= i < 30:
                    dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1], costs[2])
                else:
                    dp[i] = min(dp[i-1] + costs[0], costs[1], costs[2])
            else:
                dp[i] = dp[i-1]
        
        return dp[-1]
    
    
    
# Time: O(max(days))
# Space: O(max(days))
