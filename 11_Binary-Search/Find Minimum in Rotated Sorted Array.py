# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0; r = n-1; res = nums[0]
        
        while l <= r:
            mid = l + (r - l) // 2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                res = min(res, nums[l])
                l = mid + 1
            else:
                r = mid - 1

        return res
    
    
# Time: O(log(N))
# Space: O(1)
