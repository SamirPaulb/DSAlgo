# https://leetcode.com/problems/middle-of-the-linked-list

# Method 1
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

   
# Method 2
class Solution:
    def middleNode(self, head):
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        mid = length//2
        cur = head
        for i in range(mid):
            cur = cur.next
        return cur
