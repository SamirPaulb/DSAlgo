import collections
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        @lru_cache(None)
        
        def dfs(i, j, k):
            if i >= n1 and j >= n2:
                return True
            if i < n1 and s1[i] == s3[k] and dfs(i+1, j, k+1):
                return True
            if j < n2 and s2[j] == s3[k] and dfs(i, j+1, k+1):
                return True
            else:
                return False
        
        return collections.Counter(s1 + s2) == collections.Counter(s3) and dfs(0, 0, 0)