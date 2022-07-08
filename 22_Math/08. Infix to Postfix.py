# https://practice.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1#
'''
Input: str = "a+b*(c^d-e)^(f+g*h)-i"
Output: abcd^e-fgh*+^*+i-
'''

class Solution:
    def InfixtoPostfix(self, exp):
        res = ""
        stack = []
        priorityOrder = {'+':0, '-':0, '*':1, '/':1, '^':2}
        
        for c in exp:
            if c not in '+-*/^()':
                res += c
            elif c == "(":
                stack.append(c)
            elif c == ")":
                op = stack.pop()
                while stack and op != "(":
                    res += op
                    op = stack.pop()
            else:
                while stack and stack[-1] in priorityOrder and priorityOrder[c] <= priorityOrder[stack[-1]]:
                    res += stack.pop()
                stack.append(c)
                    
        while stack:
            res += stack.pop()
            
        return res
    
