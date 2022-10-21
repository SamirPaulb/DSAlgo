class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cp = 1         # current product
        mp = nums[0]   # maximum product
        
        for i in nums:
            cp *= i
            mp = max(mp, cp, i)
            if cp == 0: 
                cp = 1
        
        cp = 1
        for i in nums[::-1]:
            cp *= i
            mp = max(mp, cp, i)
            if cp == 0: 
                cp = 1
        
        return mp