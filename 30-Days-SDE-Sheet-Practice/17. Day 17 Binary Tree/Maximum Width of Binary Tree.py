# https://leetcode.com/problems/maximum-width-of-binary-tree/

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append((root, 0))
        
        res = 0
        if not root: return res
        # Draw the Full Binary Tree and place given tree's nodes. We see that  
        # current node's index is parent node's_index * 2  
        while q:
            # q[0] is left-most and q[-1] is right-most node of current level
            res = max(res, q[-1][1] - q[0][1] + 1)
            n = len(q)
            for i in range(n):
                tmp = q.popleft()
                node = tmp[0]
                dist = tmp[1]
                if node.left: q.append((node.left, 2*dist-1))
                if node.right: q.append((node.right, 2*dist))
        
        return res
    
# Time: O(N)
# Space: O(N)

