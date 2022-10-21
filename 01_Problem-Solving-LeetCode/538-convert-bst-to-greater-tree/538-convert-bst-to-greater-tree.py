# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.s = 0
        
        def rightRootLeft(root):
            if not root: return
            rightRootLeft(root.right)
            self.s += root.val
            root.val = self.s
            rightRootLeft(root.left)
        
        rightRootLeft(root)
        return root
    