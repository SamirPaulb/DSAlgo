class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        
        for i in range(1, len(nums)):
            if nums[prev] != nums[i]:
                prev += 1
                nums[prev] = nums[i]
        
        return prev + 1