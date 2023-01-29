# https://leetcode.com/problems/burst-balloons/
# https://youtu.be/VFskby7lUbw

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[-1]*len(nums) for _ in range(len(nums))]
        
        def dfs(l, r):
            if l > r: return 0
            if dp[l][r] != -1: return dp[l][r]
            dp[l][r] = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]  # Burst i'th balloon last
                coins += dfs(l, i-1) + dfs(i+1, r)
                dp[l][r] = max(dp[l][r], coins)
            return dp[l][r]
        
        return dfs(1, len(nums)-2)
    
    
# Time: O(N^3)
# Space: O(N^2)
