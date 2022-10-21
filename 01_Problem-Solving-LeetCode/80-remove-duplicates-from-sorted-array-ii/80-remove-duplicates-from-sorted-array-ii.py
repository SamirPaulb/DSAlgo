class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 1
        pre = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == pre: 
                c += 1
                if c > 2: nums[i] = '_'
            else:
                pre = nums[i]
                c = 1
        # print(nums)
        
        l = r = 0
        while l < len(nums):
            while l < len(nums) and nums[l] != '_':
                l += 1
            r = l
            while r < len(nums) and nums[r] == '_':
                r += 1
                
            if l < len(nums) and r < len(nums):
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
        
        n = nums.count('_')
        for _ in range(n):
            nums.pop()
            
        
        