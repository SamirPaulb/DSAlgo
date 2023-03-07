# https://leetcode.com/problems/burst-balloons/
# https://youtu.be/uG_MtaCJIrM

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[-1]*302 for _ in range(302)]
        
        def solve(l, r):
            if l > r: return 0
            if dp[l][r] != -1: return dp[l][r]
            ans = 0
            for k in range(l, r+1):
                tmp = nums[l-1] * nums[k] * nums[r+1]
                tmp += solve(l, k-1) + solve(k+1, r)
                ans = max(ans, tmp)
            dp[l][r] = ans
            return dp[l][r]
        
        return solve(1, len(nums)-2)
    
    
# Time: O(N^3)
# Space: O(N^2)
