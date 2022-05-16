# https://leetcode.com/problems/combination-sum-ii/
''' 
At each index we have 2 options. Either keep the current element or skip the current element.
Make a recursion tree of this selection. We can select an element multiple times so one call 
with same index another call from next index.
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def solve(i, target, path):
            if target == 0:
                res.append(path)
                return
            if i >= len(candidates) or target < 0: return
            
            solve(i+1, target-candidates[i], path + [candidates[i]])
            # As we can use 1 index only onece and duplecate possible
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            solve(i+1, target, path)
        
        solve(0, target, [])
        return res

# Time: O(2^N)
# Space: O(2^N)





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