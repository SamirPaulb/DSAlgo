class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.head
        self.head.next = node
        self.head = node

    def back(self, steps: int) -> str:
        while steps and self.head.prev:
            steps -= 1
            self.head = self.head.prev
        return self.head.val

    def forward(self, steps: int) -> str:
        while steps and self.head.next:
            steps -= 1
            self.head = self.head.next
        return self.head.val
    

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)