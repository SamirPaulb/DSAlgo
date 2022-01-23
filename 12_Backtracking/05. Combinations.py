# https://leetcode.com/problems/combinations/
# https://youtu.be/q0s6m7AiM7o

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(start, comb):
            if len(comb) >= k:
                res.append(comb)
                return
            for i in range(start, n+1):
                dfs(i+1, comb + [i])
        
        dfs(1, [])
        return res