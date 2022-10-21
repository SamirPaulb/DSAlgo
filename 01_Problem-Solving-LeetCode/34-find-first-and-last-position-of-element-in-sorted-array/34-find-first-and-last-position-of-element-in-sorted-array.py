class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        res = [-1, -1]
        if not nums: return res
        # first position
        while l <= r:
            mid = (l+r)//2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                if mid == 0 or nums[mid-1] != target: 
                    res[0] = mid
                    break
                r = mid - 1
                
        # last position
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                if mid == len(nums)-1 or nums[mid+1] != target: 
                    res[1] = mid
                    break
                l = mid + 1
                
        
        return res