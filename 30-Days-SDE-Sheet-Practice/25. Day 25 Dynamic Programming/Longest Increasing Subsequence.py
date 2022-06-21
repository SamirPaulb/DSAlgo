# https://leetcode.com/problems/longest-increasing-subsequence/

# ----------- Method 1 ------------------------------------------------------------------
# https://www.youtube.com/watch?v=odrfUCS9sQk
'''
class Solution:
    def lengthOfLIS(self, nums):
        # taking a array of length len(nums)
        # element of this array will be length of longest increasing subsequence upto that index of nums including nums[i]
        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            temp = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    temp = max(temp, dp[j])
            dp[i] = temp + 1
        
        res = 0
        for i in range(len(nums)):
            res = max(res, dp[i])
            
        return res
# Time Complexity = O(N*N/2) = O(N*N)
# Space Complexity = O(N)  # as we took a 1D array
'''
'''
# ----------- Method 2 ---------------------------------------------------------------------

# Using Binary search in DP => time optimization => O(N logN)
# https://www.youtube.com/watch?v=TocJOW6vx_I
import bisect
class Solution:
    def lengthOfLIS(self, nums):
        f = []
        for i in range(len(nums)):
            if not f or nums[i] > f[-1]:
                f.append(nums[i])
            else:
                pos = bisect.bisect_left(f, nums[i])  # this is used for binary search left most value. eg, arr = [1,2,2,2,3,4,5] here bisect.bisect_left(arr, 2) = 1 index 
                f[pos] = nums[i]
        return len(f)

# Time Complexity = O(N log(N)) 
# Space Complexity = O(N)  # as we took a 1D array
'''
# -------------- Method 3 ------------------------------------------------------------------

class Solution:
    def lengthOfLIS(self, nums):
        arr = []
        for i in range(len(nums)):
            if not arr or nums[i] > arr[-1]:
                arr.append(nums[i])
            else:
                index = self.binarySearchLeftMost(arr, nums[i])
                arr[index] = nums[i]
        return len(arr)
        
    def binarySearchLeftMost(self, arr, target):
        l = 0; r = len(arr) - 1
        while l <= r:
            mid = (l+r) // 2
            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
            
# Time Complexity = O(N log(N))
# Space Complexity = O(N)  # as we took a 1D array
        
        
        
        