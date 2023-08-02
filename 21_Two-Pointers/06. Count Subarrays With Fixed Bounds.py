# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        l = r = 0   # window size
        recentMin = recentMax = -1  # most recent instance of the minK and maxK
        while r < len(nums):
            # if any num in window is bigger or smaller ignore the whole window
            while r < len(nums) and minK <= nums[r] <= maxK:
                if nums[r] == minK:
                    recentMin = r
                if nums[r] == maxK:
                    recentMax = r
                if recentMin != -1 and recentMax != -1:
                    # we can make as many new subarrays as the earliest occurrence of recentMin or recentMax minus the starting position of our window
                    res += min(recentMin, recentMax) - l + 1
                r += 1
            recentMin = recentMax = -1
            l = r+1
            r += 1
        
        return res

    
# Time: O(N)
# Space: O(1)
