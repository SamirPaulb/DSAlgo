class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(i, path):
            if i >= len(nums):
                res.append(path)
                return 
            dfs(i+1, path + [nums[i]])
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, path)
        
        dfs(0, [])
        return res