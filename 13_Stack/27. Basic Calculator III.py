# https://www.lintcode.com/problem/849/
# https://leetcode.com/problems/basic-calculator-iii/description/
# https://medium.com/@CalvinChankf/solving-basic-calculator-i-ii-iii-on-leetcode-74d926732437


# Approach 1 ----- SAME as Basic Calculator I Approach 1 ------------------------------

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
                if c in '+-*/)' or not q:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        stack.append(int(stack.pop()/num))
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