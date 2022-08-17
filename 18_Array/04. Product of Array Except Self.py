# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        p = 1
        for i in range(1, len(nums)):
            p *= nums[i-1]
            output[i] *= p
        
        p = 1
        for i in range(len(nums)-2, -1, -1):
            p *= nums[i+1]
            output[i] *= p
        
        return output
      
      
# Time: O(N)
# Space: O(1)
