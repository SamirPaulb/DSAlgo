# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        sign = "+"
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = ""
                while i < len(s) and s[i].isdigit():
                    num += s[i]
                    i += 1
                i -= 1
                num = int(num)
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    newNum = math.trunc(stack.pop() / num)
                    # or can use newNum = int(stack.pop() / num)
                    # for negative numbers // will not work; e.g. s = "14-3/2", output = 13
                    stack.append(newNum)
            elif s[i] in "+-*/":
                sign = s[i]
            i += 1
        
        return sum(stack)
                
