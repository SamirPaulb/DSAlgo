# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:     # O(1)
        self.stack = [x] + self.stack
        
    def pop(self) -> int:               # O(1)
        return self.stack.pop()

    def peek(self) -> int:              # O(1)
        return self.stack[-1]

    def empty(self) -> bool:            # O(1)
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
