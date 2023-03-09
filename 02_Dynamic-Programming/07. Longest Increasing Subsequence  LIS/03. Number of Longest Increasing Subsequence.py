# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# https://youtu.be/Tuc-rjJbsXU

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)  # length of LIS
        count = [1]*len(nums)   # count of LIS
        
        for r in range(len(nums)):
            for l in range(r):
                if nums[l] < nums[r] and dp[l] + 1 > dp[r]:
                    dp[r] = dp[l] + 1
                    count[r] = count[l]  # inherit count
                elif nums[l] < nums[r] and dp[l] + 1 == dp[r]:
                    count[r] += count[l] # increase the count
        
        maxi = max(dp)
        res = 0
        for i in range(len(nums)):
            if dp[i] == maxi:
                res += count[i]
        # print(nums)    # [1, 5, 4, 3, 2, 6, 7,10, 8, 9]
        # print(dp)      # [1, 2, 2, 2, 2, 3, 4, 5, 5, 6]
        # print(count)   # [1, 1, 1, 1, 1, 4, 4, 4, 4, 4]
        return res
    
    
    
    
# Time: O(N^2)
# Space: O(N)
