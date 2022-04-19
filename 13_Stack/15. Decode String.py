# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []; curNum = 0; curString = ''
        
        for ch in s:
            if ch.isdigit():
                curNum = curNum * 10 + int(ch)
            
            elif ch == '[':
                stack.append(curString)
                stack.append(curNum)
                curNum = 0
                curString = ''
            
            elif ch == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
                
            else:
                curString += ch
        
        return curString
    
# Time: O(N)
# Space: O(N)