# https://leetcode.com/problems/arithmetic-slices/

'''# observe the sequence
In arr assume index (r - l) is max length of arithmetic subarray.
for length = 3; number of arithmetic subarrays = 1
for length = 4; number of arithmetic subarrays = 3
for length = 5; number of arithmetic subarrays = 6
for length = 6; number of arithmetic subarrays = 10
for length = 7; number of arithmetic subarrays = 15

nums = [1, 2, 3, 4, 5, 6,  7]
arr  = [0, 0, 1, 3, 6, 10, 15]

'''


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        if n == 3: return 1
        arr = [0] * (n+1)
        arr[3] = 1
        for i in range(4, n+1):
            arr[i] = arr[i-1] + (i-3+1)
        # print(arr)
        res = 0
        l = 0; r = 1; diff = nums[r] - nums[l]
        while r < n:
            if nums[r] - nums[r-1] != diff:
                diff = nums[r] - nums[r-1] 
                res += arr[r-l]
                l = r-1
            r += 1
        res += arr[r-l]
        return res
      
      
      
# Time: O(N)
# Space: O(N)
