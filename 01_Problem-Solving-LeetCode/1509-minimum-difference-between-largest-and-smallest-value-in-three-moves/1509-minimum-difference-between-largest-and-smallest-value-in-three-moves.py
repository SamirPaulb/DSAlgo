class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4: return 0
        
        nums.sort()
        res = nums[-1] - nums[0]
        
        for i in range(4):
            res = min(res, nums[n-4+i] - nums[i])
        
        return res