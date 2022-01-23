# https://leetcode.com/problems/remove-invalid-parentheses/

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        
        def solution(st, mra):   # mra = Minimum Removal Allowed
            if mra == 0:
                mrnow = self.minRemovalAllowed(st)   # mrnow = Minimum Removal Allowed Now with the string
                if mrnow == 0:
                    res.add(st)
                return
            for i in range(len(st)):
                newSt = st[:i] + st[i+1:]
                solution(newSt, mra - 1)
        
        mra = self.minRemovalAllowed(s)
        solution(s, mra)
        if len(res) == 0: res.add("")
        return res
        
        
    def minRemovalAllowed(self, s):
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            elif i == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(i)
                    
        return len(stack)
        