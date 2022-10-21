class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0; r = len(nums)-1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target: return mid
            
            if nums[l] <= nums[mid]:       # Left subarray of mid is sorted
                if nums[l] <= target < nums[mid]:  # target present at Left subarray of mid 
                    r = mid - 1
                else:                      # target at right subarray of mid
                    l = mid + 1
                    
            else:                          # right subarray of mid is sorted
                if nums[mid] < target <= nums[r]:  # target is present at right subarray of mid
                    l = mid + 1            
                else:                      # target at left subarray of mid
                    r = mid - 1
        
        return -1  # target is not present in nums