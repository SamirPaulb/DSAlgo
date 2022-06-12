# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        s = 0
        res = 0
        for r in range(len(nums)):
            s += nums[r]
            while s * (r - l + 1) >= k:
                s -= nums[l]
                l += 1
            res += r - l + 1
        
        return res

# Time: O(N)
# Space: O(1)

