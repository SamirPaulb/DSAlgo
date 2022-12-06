# https://leetcode.com/problems/largest-divisible-subset
  
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        numDict = {num:[num] for num in nums}

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(numDict[nums[i]]) < len(numDict[nums[j]]) + 1:
                    numDict[nums[i]] = numDict[nums[j]] + [nums[i]]
        
        res = []
        for num in numDict:
            if len(numDict[num]) > len(res):
                res = numDict[num]

        return res
      
      
# Time: O(N^2)
# Space: O(N^2)
