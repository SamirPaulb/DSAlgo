# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOR = 0
        for i in nums:
            maxOR |= i
        
        def dfs(i, val):
            if val == maxOR: return 1 << (len(nums)-i)
            if i == len(nums): return 0
            return dfs(i+1, val | nums[i]) + dfs(i+1, val)
        
        return dfs(0, 0)
