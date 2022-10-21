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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        
        q = [root]
        while q:
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                if i == n-1: node.next = None
                else: node.next = q[0]
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return root