class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        res = 0
        for i in s:
            if not stack:
                stack.append(i)
                res += 1
            elif stack[-1] == "R" and i == "L":
                stack.pop()
            elif stack[-1] == "L" and i == "R":
                stack.pop()
            else:
                stack.append(i)
                
        return res