# https://leetcode.com/problems/combination-sum/
''' 
At each index we have 2 options. Either keep the current element or skip the current element.
Make a recursion tree of this selection. We can select an element multiple times so one call 
with same index another call from next index.
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def solve(i, target, path):
            if target == 0:
                res.append(path)
                return
            if target < 0 or i >= len(candidates): return
            
            solve(i, target-candidates[i], path + [candidates[i]])
            solve(i+1, target, path)
            
        solve(0, target, [])
        return res
        
# Time and space complexity of this problem if not fixed. But below is the hypothetical time and space
# Time: O(2^t * n) ; where t = target/candidate[i] ; n = len(candidates)
# Space: O(nCk)  ; where n = len(candidates) ; k = number of combinations
# k depends on the values of candidates as if large value more quickly target can be achived and less length
