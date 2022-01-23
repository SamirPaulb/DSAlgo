# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n):
        res = []
        
        def dfs(openP, closeP, path):
            if openP == closeP == n:
                res.append(path)
                
            if openP < n:
                dfs(openP+1, closeP, path + "(")
                
            if openP > closeP:
                dfs(openP, closeP+1, path + ")")
        
        dfs(0, 0, "")
        return res