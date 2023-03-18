# https://leetcode.com/problems/design-browser-history/ 


# Method 1 --------- Doubly LinkedList ---------

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
            self.head = self.head.prev
            steps -= 1
        return self.head.val

    def forward(self, steps: int) -> str:
        while steps and self.head.next:
            self.head = self.head.next
            steps -= 1
        return self.head.val
    

    
    
    
# Method 2 --------- Array ---------

class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.pages = self.pages[:self.i+1] + [url]
        self.i += 1

    def back(self, steps: int) -> str:
        for i in range(steps):
            self.i -= 1
        if self.i < 0: self.i = 0
        return self.pages[self.i]
        
    def forward(self, steps: int) -> str:
        for i in range(steps):
            self.i += 1
        if self.i >= len(self.pages): self.i = len(self.pages)-1
        return self.pages[self.i]
    
