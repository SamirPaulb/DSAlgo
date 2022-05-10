# https://leetcode.com/problems/delete-node-in-a-linked-list/

'''
We are given only the node. the head is not given.
So instead of deleting the given node delete the next node of change the value of
the given node with the next node's value. 
But this approach only change the value of the given node not link with previous node.
'''

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

# Time: O(1)
# Space: O(1)
        