class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = ListNode(-1, -1)
        self.right = ListNode(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def makeMRU(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node
    
    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self.delete(node)
        self.makeMRU(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.makeMRU(self.cache[key])
        if len(self.cache) > self.capacity:
            del self.cache[self.left.next.key]
            self.delete(self.left.next)
        

