# https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.res = 2**31
        children = [0] * k
        def dfs(i):
            if i >= len(cookies):
                self.res = min(self.res, max(children))
                return
            if max(children) > self.res: return
            for j in range(k):
                children[j] += cookies[i]
                dfs(i+1)
                children[j] -= cookies[i]
                
        dfs(0)
        return self.res

# Time: O(n^k)
# Space: O(k)

