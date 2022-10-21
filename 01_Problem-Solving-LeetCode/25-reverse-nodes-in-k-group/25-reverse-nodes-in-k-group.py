class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1: return head
        
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        
        countOfNodes = 0
        while head:
            head = head.next
            countOfNodes += 1
        
        while countOfNodes >= k:
            cur = pre.next
            nex = cur.next
            for i in range(k-1):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            pre = cur
            countOfNodes -= k
        
        return dummy.next