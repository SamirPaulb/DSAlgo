# https://leetcode.com/problems/subsets-ii/

# Use the same concept of 01. Subset Sums

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset)
                return
            
            dfs(i+1, subset + [nums[i]])
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, subset)
        
        dfs(0, [])
        return res
            

# Time: O(2^n)
# Space: O(2^n)  # as we are storeing subsets in path array in each calls