class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign, stack = 0, 0, 1, []
        
        for ch in s:
            if ch.isdigit():
                num = num*10 + ord(ch) - ord('0') 
                
            elif ch in ['+', '-']:
                res += sign * num
                num = 0
                sign = 1 if ch == '+' else -1
        
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            
            elif ch == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        
        return res + sign * num

# Time: O(N)
# Space: O(N)
                