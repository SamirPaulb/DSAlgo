# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if not stack: stack.append(i)
                
            elif stack[-1] == "(" and i == ")": stack.pop()
            
            elif stack[-1] == "{" and i == "}": stack.pop()
            
            elif stack[-1] == "[" and i == "]": stack.pop()
            
            else: stack.append(i)
        
        return len(stack) == 0

