# https://leetcode.com/problems/maximum-erasure-value/


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l, r = 0, 1
        res = tmp = nums[0]
        subarr = {nums[0]}
        for r in range(1, len(nums)):
            while nums[r] in subarr:
                subarr.remove(nums[l])
                tmp -= nums[l]
                l += 1
            tmp += nums[r]
            subarr.add(nums[r])
            res = max(res, tmp)
        
        return res
    
    
# Time: O(N)
# Space: O(N)
