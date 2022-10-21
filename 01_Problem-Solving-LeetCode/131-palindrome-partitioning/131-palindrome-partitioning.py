class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def solve(s, path):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    solve(s[i:], path + [s[:i]])
        
        solve(s, [])
        return res