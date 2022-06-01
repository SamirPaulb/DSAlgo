# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Morris Traversal Flatten Binary Tree to Linked List - Preorder 

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:
            if not cur.left:
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur.right
                    cur.right = cur.left
                    cur.left = None
                    cur = cur.right
                else:
                    cur = cur.right

                    
# Time: O(N)
# Space: O(1) ; as we have not used any extra space only changed the links b/w nodes

