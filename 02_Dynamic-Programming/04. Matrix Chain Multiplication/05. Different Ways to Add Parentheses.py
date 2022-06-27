# https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def clac(a, b, operator):
            if operator == "+": return a + b
            if operator == "-": return a - b
            if operator == "*": return a * b
            
        memo = {}        
        def solve(expr):
            if expr.isdigit(): return [int(expr)]
            if expr in memo: return memo[expr]
            res = []
            for i in range(len(expr)):
                if expr[i] in "+-*":
                    left = solve(expr[:i])
                    right = solve(expr[i+1:])
                    for a in left:
                        for b in right:
                            res.append(clac(a, b, expr[i]))
            memo[expr] = res
            return memo[expr]
        
        return solve(expression)
