# https://leetcode.com/problems/reverse-nodes-in-k-group/
''' 
Apply the concept of reverse LinkedList in a range of length K.
'''

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        
        pre = dummy
        while count >= k:
            cur = pre.next
            nex = cur.next
            for i in range(k-1):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            pre = cur
            count -= k
            
        return dummy.next

# Time: O(N)
# Space: O(1)