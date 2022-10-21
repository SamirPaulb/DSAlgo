class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        maxReachableIndex = 0
        while r < len(nums)-1:
            for i in range(l, r+1):
                maxReachableIndex = max(maxReachableIndex, i + nums[i])
            l = r + 1
            r = maxReachableIndex
            res += 1
        
        return res
            
        