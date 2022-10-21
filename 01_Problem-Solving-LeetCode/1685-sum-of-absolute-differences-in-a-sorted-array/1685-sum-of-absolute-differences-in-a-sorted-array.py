class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        n = len(nums)
        curSum = 0
        res = [0]*n
        
        for i in range(len(nums)):
            res[i] = ((i*nums[i])-curSum) + ((s-curSum-nums[i])-(n-i-1)*nums[i])
            curSum += nums[i]
            
        return res