# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        sign = '+'
        stack = []
        
        i = 0
        while i < n:
            if s[i].isdigit():
                num = s[i]
                i += 1
                while i < n and s[i].isdigit():
                    num += s[i]
                    i += 1
                i -= 1
                num = int(num)
                
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    newNum = stack.pop() * num
                    stack.append(newNum)
                elif sign == '/':
                    newNum = math.trunc(stack.pop() / num)
                    # or can use newNum = int(stack.pop() / num)
                    # for negative numbers // will not work
                    stack.append(newNum)
                
            elif s[i] != ' ':
                sign = s[i]
            i += 1
        
        return sum(stack)


# Time: O(N)
# Space: O(N)
        