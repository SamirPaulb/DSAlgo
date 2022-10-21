class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        r = len(nums)
        l = 0
        
        while l <= r:
            m = (l + r) // 2
            if m == 0 or m == len(nums)-1: return nums[m]
            
            if m % 2 != 0:
                if nums[m-1] != nums[m] != nums[m+1]: 
                    return nums[m]
                elif nums[m-1] != nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m-1] != nums[m] != nums[m+1]:
                    return nums[m]
                elif nums[m] != nums[m+1]:
                    r = m - 1
                else: 
                    l = m + 1
                    
        return nums[m]