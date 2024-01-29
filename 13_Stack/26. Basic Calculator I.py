# https://leetcode.com/problems/basic-calculator/

# Approach 1 ----- Can be used in Basic Calculator III -------------------------------

import collections
class Solution:
    def calculate(self, s: str) -> int:
        def helper(q):
            stack = []
            sign = '+'
            num = 0
            while q:
                c = q.popleft()
                if c.isdigit():
                    num = num*10 + int(c)
                if c == '(':
                    num = helper(q)
                if c in '+-)' or not q:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    sign = c
                    num = 0
                    if c == ')':
                        break
            return sum(stack)

        q = collections.deque()
        for c in s:
            q.append(c)

        return helper(q)
        

# Time: O(N)
# Space: O(N)


# Approach 2 --------------------------------------------------------------------------

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
                