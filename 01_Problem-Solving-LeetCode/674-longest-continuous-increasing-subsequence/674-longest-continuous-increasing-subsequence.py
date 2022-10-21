class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = tmp = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                tmp += 1
                res = max(res, tmp)
            else:
                tmp = 1
            
        return res