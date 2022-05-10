#### https://leetcode.com/problems/linked-list-cycle-ii/


Take two pointers, fast and slow. Fast goes two steps ahead while slow pointer does single step ahead for each iteration. If a cycle exists, fast and slow pointers will collide. 
Take another pointer, say check. Move the slow and the check pointers ahead by single steps until they collide. Once they collide we get the starting node of the linked list


Proof of Why check and slow will collide at the node where loop started.↓ 👇
<a href="#"><img width="100%" height="50%" src="https://raw.githubusercontent.com/SamirPaulb/assets/main/LinkedList-Cycle-II-find-point-where-loop-started.jpg" /></a>

```python

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        isCycle = False
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                isCycle = True
                break
        
        if not isCycle: return None
        
        check = head
        while check != slow:
            slow = slow.next
            check = check.next
        
        return check

# Time: O(N)
# Space: O(1)
```
