# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        def solve(node):
            while node:
                q = node.next
                if not q: tail = node
                if node.child:
                    node.next = node.child
                    node.child.prev = node
                    t = solve(node.child)
                    t.next = q
                    if q: q.prev = t
                    node.child = None
                node = node.next
            return tail
        
        solve(head)
        return head
    
# Time: O(N); where N is total number of nodes in the Doubly Linked List
# Space: O(1)

