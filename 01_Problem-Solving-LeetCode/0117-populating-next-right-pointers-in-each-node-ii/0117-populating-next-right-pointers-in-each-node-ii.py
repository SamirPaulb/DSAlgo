"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        q = collections.deque([root])
        
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i < n-1: node.next = q[0]
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return root