class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        curSum = 0
        res = 0
        
        for r in range(len(nums)):
            curSum += nums[r]
            while l <= r and curSum * (r - l + 1) >= k:
                curSum -= nums[l]
                l += 1
            res += (r - l + 1)
        
        return res