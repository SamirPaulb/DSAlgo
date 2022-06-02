# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack: self.stack.append([val, val])
        else: self.stack.append([val, min(self.stack[-1][1], val)])

    def pop(self) -> None:
        return self.stack.pop()[1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Time: O(1)
# Space: O(1)