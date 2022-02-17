# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums):
        # in Circle 1st house is neighbor of last house
        if len(nums) < 2: return max(nums)
        
        def houseRobber1(nums):
            n = len(nums)
            if n < 2: return max(nums)
            dp = [0] * (n+1)
            dp[1] = nums[0]
            for i in range(2, n+1):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
            return dp[-1]
        
        res1 = houseRobber1(nums[1:])           # house robber1 excluding 1st house
        res2 = houseRobber1(nums[:len(nums)-1]) # house robber1 excluding Last house
        
        return max(res1, res2)

        