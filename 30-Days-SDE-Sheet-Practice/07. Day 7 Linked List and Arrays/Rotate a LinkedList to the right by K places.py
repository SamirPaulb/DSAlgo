# https://leetcode.com/problems/rotate-list/
''' 
With 2 pointer approach go to the (length - K)th node the disconnect right part
and connect it to the front head. return the new head(ie. node where we disconnected)  
'''
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k: return head
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        
        k = k % count
        
        fast = head
        slow = head
        while fast:
            if k >= 0:
                fast = fast.next
                k -= 1
            else:
                fast = fast.next
                slow = slow.next
        
        end = slow.next
        slow.next = None
        cur = end
        while cur and cur.next:
            cur = cur.next
        if not end: return head
        cur.next = head
        return end
    
# Time: O(N)
# Space: (1)