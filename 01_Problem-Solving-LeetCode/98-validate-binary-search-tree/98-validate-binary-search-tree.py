# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(l, root, r):
            if not root: return True
            if not  l < root.val < r: return False
            return check(l, root.left, root.val) and check(root.val, root.right, r)
        
        return check(float('-inf'), root, float('inf'))