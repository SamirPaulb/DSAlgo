class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        l = 0 
        r = len(nums)-1
        
        while l <= r:
            ptrSum = nums[l] + nums[r]
            
            if ptrSum > target:
                r -= 1
            else:
                res += pow(2, (r - l), (10**9 + 7))
                l += 1
        
        return res % (10**9 + 7)