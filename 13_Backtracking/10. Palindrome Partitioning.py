# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s):
        res = []
        
        def isPal(s):
            return s == s[::-1]
        
        def dfs(s, path):
            if not s:
                res.append(path)
                return
            
            for i in range(1, len(s)+1):
                if isPal(s[:i]): 
                    dfs(s[i:], path + [s[:i]])
        
        
        dfs(s, [])
        return res
            