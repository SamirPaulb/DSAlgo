# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        curCount = 1
        leftPre = dummy
        rightNex = head
        
        while cur:
            if curCount < left:
                leftPre = leftPre.next
            if curCount == right:
                rightNex = cur.next
                cur.next = None
                break
            cur = cur.next
            curCount += 1
        
        pre = leftPre
        cur = pre.next
        nex = cur.next
        while nex:
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = cur.next
        
        cur.next = rightNex
        return dummy.next