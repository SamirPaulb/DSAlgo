# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        
        def solve(root):
            if not root: return
            solve(root.right)
            self.sum += root.val
            root.val = self.sum
            solve(root.left)
        
        solve(root)
        return root