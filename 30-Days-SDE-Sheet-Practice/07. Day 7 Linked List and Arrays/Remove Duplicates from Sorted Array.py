# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
''' 
take 2 pointers prev and cur. prev will only increase for different values. so the resulting array 
will be of unique value.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        
        for i in range(1, len(nums)):
            if nums[prev] != nums[i]:
                prev += 1
                nums[prev] = nums[i]
        
        return prev + 1

# Time: O(n)
# Space: O(1)