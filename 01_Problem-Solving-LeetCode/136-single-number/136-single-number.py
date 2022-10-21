class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        
        return res