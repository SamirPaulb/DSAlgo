# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        p = 1
        res = 0
        for r in range(len(nums)):
            p *=  nums[r]
            while l <= r and p >= k:
                p //= nums[l]
                l += 1
            res += r - l + 1
        
        return res
    
# Time: O(N)
# Space: O(1)