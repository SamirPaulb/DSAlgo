# https://leetcode.com/problems/wiggle-sort-ii/

class Solution:
    def wiggleSort(self, nums):
        arr = sorted(nums)
        
        # Putting largest element into odd index
        for i in range(1, len(nums), 2):
            nums[i] = arr.pop()
            
        # Putting remaining element into even index
        for i in range(0, len(nums), 2):
            nums[i] = arr.pop()
        
        return nums
