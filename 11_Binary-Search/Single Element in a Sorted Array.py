# https://leetcode.com/problems/single-element-in-a-sorted-array/
'''
If every element in the sorted array were to appear exactly twice, they would occur in pairs at indices i, i+1 for all even i.

Equivalently, nums[i] = nums[i+1] and nums[i+1] != nums[i+2] for all even i.

When we insert the unique element into this list, the indices of all the pairs following it will be shifted by one, negating the above relationship.
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        r = len(nums)
        l = 0
        
        while l <= r:
            m = (l + r) // 2
            if m == 0 or m == len(nums)-1: return nums[m]
            
            if m % 2 != 0:
                if nums[m-1] != nums[m] != nums[m+1]: 
                    return nums[m]
                elif nums[m-1] != nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m-1] != nums[m] != nums[m+1]:
                    return nums[m]
                elif nums[m] != nums[m+1]:
                    r = m - 1
                else: 
                    l = m + 1
                    
        return nums[m]
    
# Time: O(log(n))
# Space: O(n)
