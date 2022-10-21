class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        mini = val
        if self.stack: mini = min(mini, self.stack[-1][1])        
        self.stack.append([val, mini])

    def pop(self) -> None:
        if not self.stack: return
        self.stack.pop()

    def top(self) -> int:
        if not self.stack: return
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack: return
        return self.stack[-1][1]

