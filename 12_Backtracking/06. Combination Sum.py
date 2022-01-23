# https://leetcode.com/problems/combination-sum/

# ------------------------------ Method - Like Combination Problem ------------------------------------
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(start, comb):
            if sum(comb) == target:
                res.append(comb)
                return
            if sum(comb) > target: return   # if we keep taking current element multiple time then once sum of combination will cross target. Now Stop calling dfs
            if start >= len(candidates): return  # list index out of bound
            
            for i in range(start, len(candidates)):  # starting i from start to include current element multiple time
                dfs(i, comb + [candidates[i]])  
                
        dfs(0, [])
        return res
# Time Complexity: O(n * nCk) = O(N * N^k)
# Space Complexity: O(N)

# ------------------------------- Method - Like Subsets Problem ---------------------------------------
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, comb):
            if sum(comb) == target:
                res.append(tuple(comb))
                return
            if sum(comb) > target: # if we keep taking current element multiple time then once sum of combination will cross target. Now Stop calling dfs
                return
            if i >= len(candidates): return   # list index out of bound
            
            dfs(i, comb + [candidates[i]])   # Including the current element call to Include it again repetadely
            dfs(i+1, comb + [candidates[i]]) # currrent element will be Included only once
            dfs(i+1, comb)   # Not including current element
        
        dfs(0, [])
        return set(res)

# Time Complexity: O(n * nCk) = O(N * N^k)
# Space Complexity: O(N)