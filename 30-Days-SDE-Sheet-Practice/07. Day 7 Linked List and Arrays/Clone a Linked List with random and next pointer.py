# https://leetcode.com/problems/copy-list-with-random-pointer/
''' 
In a dictionary store the new copy nodes. Then in another traversal connect the links of 
the new nodes. 
'''

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        oldToCopy = {None : None}
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]

# Time: O(N)
# Space: O(N)