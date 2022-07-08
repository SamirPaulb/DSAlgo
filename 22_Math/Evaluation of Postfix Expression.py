# https://practice.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1/#

class Solution:
    def evaluatePostfix(self, S):
        stack = []
        for i in S:
            if i in "*/+-":
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    val = self.calculate(a, b, i)
                    stack.append(val)
            else:
                stack.append(i)
        
        return "".join(stack)
        
    def calculate(self, a, b, ope):
        a = int(a); b = int(b)
        if ope == "+": return str(a + b)
        if ope == "-": return str(a - b)
        if ope == "*": return str(a * b)
        if ope == "/": return str(a // b)
