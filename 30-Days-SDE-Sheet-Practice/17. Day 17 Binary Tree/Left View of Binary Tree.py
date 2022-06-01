# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1#

import collections

def LeftView(root):
    final_ans = []
    q = collections.deque()
    q.append(root)
    if not root: return final_ans
				
    while q:
        final_ans.append(q[0].data)
        n = len(q)
        for i in range(n):
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
    return final_ans
        
# Instead of using array as a queue we should use collections.deque()
# as pop() 0'th element from deque is of O(1) time.

# Time: O(N)
# Space: O(N)
