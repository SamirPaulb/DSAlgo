# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:

        def calculate(sign, num):
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
        
        stack = []
        sign = '+'
        num = 0
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            elif i in '+-*/':
                calculate(sign, num)
                num = 0
                sign = i
        
        calculate(sign, num) 
        return sum(stack)

# Time: O(N)
# Space: O(N)