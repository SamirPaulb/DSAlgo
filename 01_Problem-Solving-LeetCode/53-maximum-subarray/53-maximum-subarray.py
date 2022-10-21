class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs = 0
        ms = nums[0]
        
        for num in nums:
            cs += num
            cs = max(cs, num)
            ms = max(ms, cs)
        
        return ms