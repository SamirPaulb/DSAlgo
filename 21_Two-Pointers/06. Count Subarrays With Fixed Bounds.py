# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        r = 0 # right of window
        l = 0 # left of window
        n = len(nums)
        recentMin = -1 # most recent instance of the max
        recentMax = -1 # most recent instance of the min
        while r < n:
            while r<n: # sliding to the right
                num = nums[r]
                if not minK<=num<=maxK: # if this number is too big or small we can no longer use this window
                    break
                # now update the recent min and max if needed
                if num == minK:
                    recentMin = r
                if num == maxK:
                    recentMax = r
                r += 1
                if recentMin != -1 and recentMax != -1:
                    ans += (min(recentMin,recentMax)-l)+1 # we can make as many new subarrays as the earliest occurrence of recentMin or recentMax minus the starting position of our window
            # reset everything
            r+=1
            l = r
            recentMin = -1
            recentMax = -1
            
        return ans
    
    
# Time: O(N)
# Space: O(1)
