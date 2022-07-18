# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self._deque = collections.deque()

    def push(self, x: int) -> None:
        self._deque.append(x)
        for _ in range(len(self._deque)-1):
            self._deque.append(self._deque.popleft())

    def pop(self) -> int:
        return self._deque.popleft()

    def top(self) -> int:
        return self._deque[0]

    def empty(self) -> bool:
        return len(self._deque) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
