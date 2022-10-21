class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        s = e = ''        
        i = 0
        
        while i < len(nums):
            s = str(nums[i])
            i += 1
            while i < len(nums) and nums[i]-1 == nums[i-1]:
                e = '->' + str(nums[i])
                i += 1
            res.append(s + e)
            s = e = ''
        
        return res
                
        
# Time: O(N)
# Space: O(1)