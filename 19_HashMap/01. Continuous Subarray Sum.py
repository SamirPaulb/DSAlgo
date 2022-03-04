# https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sumIndexDic = {0 : -1}    # nums = [14, 7]; k = 7
        curSum = 0
        
        for i in range(len(nums)):
            curSum += nums[i]
            curSum = curSum % k
            
            if curSum in sumIndexDic:
                if i - sumIndexDic[curSum] >= 2: 
                    return True
            else:
                sumIndexDic[curSum] = i
        
        return False