# https://leetcode.com/problems/two-sum/
''' 
Keep a track of traversed element in a dictionary. If we get the target - nums[i] then we got the 2 indeces
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i in range(len(nums)):
            required = target - nums[i]

            if required in dic:
                return [dic[required], i]

            dic[nums[i]] = i