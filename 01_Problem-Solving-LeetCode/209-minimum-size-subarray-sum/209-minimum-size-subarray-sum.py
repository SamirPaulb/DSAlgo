class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target > sum(nums): return 0
        start = 0
        end = 0
        res = 2**31
        s = 0
        
        while end < len(nums):
            while s < target and end < len(nums):
                s += nums[end]
                end += 1
            
            while s >= target and start < end:
                res = min(res, end - start)
                s -= nums[start]
                start += 1
        
        return res