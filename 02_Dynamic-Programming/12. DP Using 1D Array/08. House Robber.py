# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums):
        '''
        # Recursive Solution
        self.res = 0
        
        def solve(nums, path):
            if not nums:
                self.res = max(self.res, path)
                return
            for i in range(len(nums)):
                solve(nums[i+2:], path + nums[i])
            
        solve(nums, 0)
        return self.res
        '''
    
        # Dynamic Programming Solution
        n = len(nums)
        dp = [0] * (n+1)
        dp[1] = nums[0]
        
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
            
        return dp[-1]
    
        # Time Complexity = O(n)
        # Space Complexity = O(n)