class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        i = -1
        count0 = 0
        
        for j in range(len(nums)):
            if nums[j] == 0: count0 += 1
            while count0 > k:
                i += 1
                if nums[i] == 0: count0 -= 1
            res = max(res, j - i)
        
        return res