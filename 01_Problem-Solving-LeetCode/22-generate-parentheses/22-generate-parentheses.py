class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(openP, closeP, path):
            if openP == closeP == n:
                res.append(path)
            if openP < n:
                backtrack(openP+1, closeP, path + '(')
            if closeP < openP:
                backtrack(openP, closeP+1, path + ')')
        
        backtrack(0, 0, '')
        return res