# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
''' 
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, 
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.
Input: root = [1,2,3,4,5,6]
Output: true

Input: root = [1,2,3,4,5,null,7]
Output: false
'''

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # The level-order traversal array of a complete binary tree will never have a null node in between non-null nodes. If we encounter a null node, all the following nodes should also be null, otherwise it's not complete.
        if not root: return True
        
        have_null = False
        q = [root]
        
        while q:
            node = q.pop(0)
            if not node: 
                have_null = True
                continue
            if have_null == True: return False
            q.append(node.left)
            q.append(node.right)
        
        return True
    
            