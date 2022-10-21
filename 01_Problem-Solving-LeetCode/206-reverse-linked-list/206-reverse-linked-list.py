# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = pre.next
        nex = cur.next
        
        while nex:
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = cur.next
        
        return dummy.next