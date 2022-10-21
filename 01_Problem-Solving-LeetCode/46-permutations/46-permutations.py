class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(nums, path):
            if not nums: 
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])
        
        dfs(nums, [])
        return res