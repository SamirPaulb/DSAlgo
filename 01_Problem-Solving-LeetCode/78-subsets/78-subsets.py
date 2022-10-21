class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        def dfs(arr, path):
            if not arr: 
                res.append(path)
                return
            dfs(arr[1:], path + [arr[0]])
            dfs(arr[1:], path)
                
        dfs(nums, [])
        return res