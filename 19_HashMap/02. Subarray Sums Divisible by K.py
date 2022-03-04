# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# https://www.youtube.com/watch?v=QM0klnvTQzk

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Use COncept of 523. Continuous Subarray Sum
        
        ans = 0
        remainderCountDic = {0 : 1}
        curSum = 0
        
        for i in range(len(nums)):
            curSum += nums[i]
            
            if curSum < 0: curSum += k
            
            curSum = curSum % k
            
            if curSum in remainderCountDic:
                ans += remainderCountDic[curSum]
                remainderCountDic[curSum] += 1
            else:
                remainderCountDic[curSum] = 1
        
        return ans