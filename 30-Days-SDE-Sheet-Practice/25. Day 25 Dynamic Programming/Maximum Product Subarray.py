# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mp = nums[0]    # max product
        cp = 1          # current product
        
        for i in nums:
            cp *= i
            mp = max(cp, mp)
            if cp == 0: cp = 1
        
        cp = 1
        for i in nums[::-1]:
            cp *= i
            mp = max(mp, cp)
            if cp == 0: cp = 1
                
        return mp



# Time: O(N)
# Space: O(N)