# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        dummy = ListNode(-103)
        dummy.next = head
        pre = dummy
        cur = dummy.next
        curPre = dummy
        
        while cur.next:
            if cur.val == cur.next.val:
                curPre = cur
                cur = cur.next
            else:
                if cur.val == curPre.val:
                    curPre = cur
                    cur = cur.next
                else:
                    curPre.next = None
                    pre.next = cur
                    pre = pre.next
                    curPre = cur
                    cur = cur.next
        
        if curPre.val == cur.val:
            cur = cur.next
            curPre.next = None
        pre.next = cur
             
        return dummy.next