# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums, k):
        # nums = [1,2,3,4,5,6,7,8,9,10]; k = 3
        n = len(nums)
        k = k % n
        
        # Step-1
        i = 0
        j = n-k-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        # nums = [7,6,5,4,3,2,1, 8,9,10]
        
        # Step-2
        # swap right k subarray with left k subarray
        i = n-k
        j = n-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        # nums = [7,6,5,4,3,2,1, 10,9,8]
        
        # Step-3
        # reverse total nums
        i = 0
        j = n-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        # nums = [8,9,10,1,2,3,4,5,6,7]        