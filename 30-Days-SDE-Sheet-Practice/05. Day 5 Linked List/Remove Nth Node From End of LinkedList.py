# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

''' 
Take a dummy node connect it with head (if we take a dummy node then it would be easy 
to delete the first node if target node is head ie. n = length of list). 
Take 2 pointers fast and slow. Increase the fast pointer by n steps. 
Then in next pass increase both slow and fast together by one step. 
Slow will stop before the target element then delete the link.
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        fast = head
        slow = dummy
        
        for i in range(n):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        tmp = slow.next.next
        slow.next.next = None
        slow.next = tmp
        
        return dummy.next

# Time: O(N)   where N is the length of the linkedlist 
# Space: O(1)
