# https://leetcode.com/problems/maximum-subarray/

''' 
Kadane’s Algorithm:
Initialize:
    max_so_far = INT_MIN
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
return max_so_far

'''

class Solution:
    def maxSubArray(self, nums):
        # Implement Kadane's Algorithm
        cs, ms = nums[0], nums[0]   # Current Sum, Maximum Sum
        for i in range(1, len(nums)):
            cs = max(cs + nums[i], nums[i])
            ms = max(cs, ms)
        
        return ms

# Time Complexity: O(n)