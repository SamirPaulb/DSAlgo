class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        
        def solve(expr):
            res = []
            if expr.isdigit():
                return [int(expr)]
            if expr in memo:
                return memo[expr]
            
            for i in range(len(expr)):
                if expr[i] in "+-*":
                    res1 = solve(expr[:i])
                    res2 = solve(expr[i+1:])
                    for j in res1:
                        for k in res2:
                            res.append(clac(j, k, expr[i]))
            return res
        
        def clac(j, k, operator):
            if operator == "+":
                return j + k
            if operator == "-":
                return j - k
            if operator == "*":
                return j * k
            return -1
        
        return solve(expression)