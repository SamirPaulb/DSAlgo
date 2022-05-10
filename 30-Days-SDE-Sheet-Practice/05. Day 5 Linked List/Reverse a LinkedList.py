# https://leetcode.com/problems/reverse-linked-list/
''' 
Use three pointers to change the links between nodes.
'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        pre = ListNode(-1)
        pre.next = head
        cur = pre.next
        nex = cur.next
        
        while nex:
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = cur.next
        
        return pre.next

