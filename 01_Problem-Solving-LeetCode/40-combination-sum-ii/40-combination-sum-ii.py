class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []
        
        def dfs(start, path, target):
            if target == 0: res.append(path); return
            if start >= n or target < 0: return
            
            prev = -1
            for i in range(start, n):
                if candidates[i] == prev: continue
                dfs(i+1, path + [candidates[i]], target - candidates[i])
                prev = candidates[i]
        
        dfs(0, [], target)
        return res