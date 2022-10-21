class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        
        for i in nums:
            a = abs(i)
            if nums[a-1] > 0: 
                nums[a-1] *= -1
        
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        
        return res