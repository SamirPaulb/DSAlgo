# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return
        self.res = root.val
        self.k = k
        
        def inorder(root):
            if not root: return
            inorder(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            inorder(root.right)
        
        inorder(root)
        return self.res