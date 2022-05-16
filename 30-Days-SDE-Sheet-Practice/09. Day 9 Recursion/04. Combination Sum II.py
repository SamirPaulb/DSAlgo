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