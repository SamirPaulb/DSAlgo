# https://leetcode.com/problems/longest-increasing-subsequence/
# https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1

# ----------- Method 1 ------------------------------------------------------------------

# https://www.youtube.com/watch?v=odrfUCS9sQk
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
                pos = bisect.bisect_left(f, nums[i])  # bisect_left function of bisect module is used to find left most value or first occurrence of target element(internally uses binary search). eg, arr = [1,2,2,2,3,4,5] here bisect.bisect_left(arr, 2) = 1 index 
                f[pos] = nums[i]
        return len(f)

# Time Complexity = O(N log(N)) # N for traversal through nums and as bisect internally uses binary search so log(N)
# Space Complexity = O(N)  # as we took a 1D array
'''
bisect is applied in sorted array

bisect.bisect_left(array, target)  => first occurrence of target in array (left most index target)
bisect.bisect_right(array, target) => Last occurrence of target in array (right most index target)

Ex: 
arr = [0, 0, 1, 1, 1, 1, 1, 5]
bisect.bisect_left(arr, 1) = 2
bisect.bisect_right(arr, 1) = 6
'''


# ----------- Method 3 ------------------------------------------------------------------

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
        
        
        
