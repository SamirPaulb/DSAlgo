class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
        def dfs(i, path, target):
            if target == 0: res.append(path)
            if target < 0 or i >= n: return
            for i in range(i, n):
                dfs(i, path + [candidates[i]], target - candidates[i])
        
        dfs(0, [], target)
        return res
    
    