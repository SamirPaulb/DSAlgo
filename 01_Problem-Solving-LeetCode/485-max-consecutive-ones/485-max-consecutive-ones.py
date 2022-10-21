class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        i = 0
        while i < len(nums):
            count = 0
            while i < len(nums) and nums[i] == 1:
                count += 1
                i += 1
            res = max(res, count)
            i += 1
        
        return res
            