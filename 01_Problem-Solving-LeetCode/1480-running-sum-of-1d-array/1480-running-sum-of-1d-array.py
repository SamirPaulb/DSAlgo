class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        Sum = 0
        for  i in range(len(nums)):
            Sum += nums[i]
            runningSum.append(Sum)
        return runningSum
            