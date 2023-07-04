# https://leetcode.com/problems/decode-string/
# https://youtu.be/qB0zZpBJlh8

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == ']':
                tmp = ""
                while stack:
                    top = stack.pop()
                    if top == '[': break
                    tmp = top + tmp
                n = int(stack.pop())
                stack.append(n*tmp)
            else:
                num = ""
                while i < len(s) and s[i].isnumeric():
                    num += s[i]
                    i += 1
                if num:
                    stack.append(num)
                stack.append(s[i])
            i += 1
        
        return "".join(stack)
    
# Time: O(N)
# Space: O(N)
