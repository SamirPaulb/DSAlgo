# https://leetcode.com/problems/arithmetic-slices/
# https://leetcode.com/problems/arithmetic-slices/solutions/1455367/Python-Bottom-up-DP-Time-O(N)-Space-O(1)-Clean-and-Concise/

# ✔️ Solution 1: Bottom up DP

class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        dp = [0] * n
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        
        return sum(dp)
    
# Time: O(n)
# Space: O(n)
    
    
# ✔️ Solution 2: Bottom up DP (Space Optimized)

class Solution:
    def numberOfArithmeticSlices(self, nums):
        dp = 0; n = len(nums); res = 0
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp += 1
                res += dp
            else:
                dp = 0
                
        return res
    
# Time: O(n)
# Space: O(1)
