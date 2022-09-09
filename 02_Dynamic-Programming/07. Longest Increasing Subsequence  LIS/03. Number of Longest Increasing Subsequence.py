# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# https://youtu.be/cKVl1TFdNXg


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        
        maxi = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    count[i] = count[j]     # inherit count
                elif nums[i] > nums[j] and dp[j] + 1 == dp[i]:
                    count[i] += count[j]    # increase the count
            maxi = max(maxi, dp[i])
            
        res = 0
        for i in range(n):
            if dp[i] == maxi:
                res += count[i]
        
        return res
    
    
# Time: O(N^2)
# Space: O(N)

