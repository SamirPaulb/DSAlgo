# https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # First Solve => Allocate Minimum Number Of Pages - Binary Search
        
        l = max(nums);  r = sum(nums);  ans = -1
        
        if len(nums) < m: return -1  # Number of elements can not be lesser than number of subarrays as we have to give atleast 1 element to a subarray

        def isValid(nums, m, mid):
            currSum = 0              # sum of elements of nums that can be allocated to one subarray
            countOfSubarrays = 1     # Number of subarrays required if mid is the max capacity of a subarray
            
            for val in nums:
                currSum += val
                if currSum > mid:          # sum of elements allocated to one subarray exceed max capacity of the subarray
                    countOfSubarrays += 1  # We need one more subarray 
                    currSum = val          # start calculating sum of elements that can be allocated to next subarray
            
            if countOfSubarrays > m: return False
            else: return True
        
        
        while l <= r:
            mid = (r+l) // 2
            if isValid(nums, m, mid):
                ans = mid            # Updating answer to current mid as current mid is the most optimized(least) ans till now
                r = mid - 1          # I will try to decrease mid
            else:
                l = mid + 1          # current mid NOT isValid so I will try to increase mid
        
        return ans                   # Most Optimized ans is stored here
            
            
            