# https://leetcode.com/problems/combination-sum-ii/

# ---------------------------------------------- Method 1 ----------------------------------------------------
# # https://youtu.be/rSA3t6BDDwg
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        
        def dfs(start, comb, target):
            if target == 0:
                res.append(comb)
                return
            if target < 0: return
            if start >= len(candidates): return
            
            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev: continue
                dfs(i+1, comb + [candidates[i]], target - candidates[i])
                prev = candidates[i]
        
        dfs(0, [], target)
        return res
# Time Complexity = 2^N  ; as for each element we have two option either include it or not include it
# Space Complexity = O(N)

# ---------------------------------------------- Method 2 ----------------------------------------------------
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = set()
        
        def dfs(start, comb):
            if sum(comb) == target:
                res.add(tuple(comb))
                return
            if sum(comb) > target: return
            if start >= len(candidates): return
            
            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev: continue
                dfs(i+1, comb + [candidates[i]])
                prev = candidates[i]
        
        dfs(0, [])
        return res

# Time Complexity = N * 2^N  ; as the sum(comb) also takes n time
# Space Complexity = O(N)