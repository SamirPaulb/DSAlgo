# https://www.lintcode.com/problem/508/
# https://leetcode.com/problems/wiggle-sort/

class Solution:
    def wiggle_sort(self, nums):
        
        for i in range(1, len(nums)):
            if  i%2 == 0 and nums[i-1] < nums[i]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            
            if i%2 == 1 and nums[i-1] > nums[i]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
        
        return nums
    
    
# Time: O(n)
# Space: O(1)
