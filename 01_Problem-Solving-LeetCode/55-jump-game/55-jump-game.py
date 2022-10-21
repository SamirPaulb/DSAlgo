class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReachable = nums[0]
        i = 0
        
        while i < len(nums) and i <= maxReachable:
            maxReachable = max(maxReachable, i + nums[i])
            if maxReachable >= len(nums)-1: return True
            i += 1
        
        return False