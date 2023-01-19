# https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        # store the indices of '('
        openStack = []
        # store the indices of '*'
        starStack = []
        
        for i, ch in enumerate(s):
            if ch == ')':
                if openStack:
                    openStack.pop()
                elif starStack:
                    starStack.pop()
                else: 
                    return False
            elif ch == '(':
                openStack.append(i)
            else:
                starStack.append(i)
                
        # cancel ( and * with valid positions, i.e., '(' must be on the left hand side of '*'
        while openStack and starStack:
            if openStack[-1] > starStack[-1]:
                return False
            openStack.pop()
            starStack.pop()
        
        # Accept when openStack is empty, which means all braces are paired
        return len(openStack) == 0
      
      
# Time: O(N)
# Space: O(N)
