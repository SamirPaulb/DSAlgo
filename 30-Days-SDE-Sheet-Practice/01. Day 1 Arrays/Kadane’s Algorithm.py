# https://leetcode.com/problems/maximum-subarray/
''' 
continuously adding new elements to cs and also checking if the current value is greater or not.
if greater then start from current element.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kaden's Algorithms
        cs = 0
        ms = nums[0]
        
        for num in nums:
            cs += num
            cs = max(cs, num)
            ms = max(ms, cs)
        
        return ms

# Time: O(N)
# Spave: O(1)