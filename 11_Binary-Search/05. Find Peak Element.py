# https://leetcode.com/problems/find-peak-element/
# https://youtu.be/OINnBJTRrMU

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        
        low = 0; high = n-1
        
        while low <= high:
            
            mid = low + (high - low) // 2
            # Instead of writting mid = (low + high)//2 we should write mid = low + (high - low)//2 because of INTEGER OVERFLOW in the former case
            
            if 0 < mid < n-1:
                if nums[mid-1] < nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid-1] > nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                    
            else:
                if mid == 0:
                    if nums[0] > nums[1]:
                        return 0
                    else:
                        return 1
                if mid == n-1:
                    if nums[n-1] > nums[n-2]:
                        return n-1
                    else:
                        return n-2
                    
# Time: O(n)
# Space: O(1)
        