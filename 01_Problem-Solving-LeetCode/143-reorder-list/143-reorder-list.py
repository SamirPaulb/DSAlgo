class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return head
        # find Mid
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        a = head
        b = mid.next
        mid.next = None
        
        # reverse b
        dummy = ListNode(-1)
        dummy.next = b
        pre = dummy
        cur = pre.next
        nex = cur.next
        while nex:
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = cur.next
        b = dummy.next
        
        # merge a and b
        while a and b:
            anext = a.next
            a.next = None
            bnext = b.next
            b.next = None
            
            a.next = b
            a = a.next
            a.next = anext
            a = a.next
            
            b = bnext
        
        return head