class Solution:
    def moveZeroes(self, nums):
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        # After this loop, nums = [1,3,12,3,12]
        
        if n >1:
            for i in range(n-count,n):
                nums[i] = 0

            #print(nums)
        
        # After this loop, nums = [1,3,12,0,0]

        
        return nums

nums = [0,1,0,3,12]

ll = Solution()
print(ll.moveZeroes(nums))
