# https://leetcode.com/problems/longest-arithmetic-subsequence/

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [{} for _ in range(len(nums))]
        res = 0
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = max(2, 1 + dp[j][diff])
                else:
                    dp[i][diff] = 2
                res = max(res, dp[i][diff])
            
        return res
    
    
# Time: O(N^2)
# Space: O(N^2)
