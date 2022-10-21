class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(i, path):
            if len(path) >= k: res.append(path); return
            for i in range(i, n+1):
                dfs(i+1, path + [i])
        
        dfs(1, [])
        return res