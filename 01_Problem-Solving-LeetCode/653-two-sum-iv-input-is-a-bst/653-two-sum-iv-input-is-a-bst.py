# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        self.res = False
        
        def inorder(root):
            if not root: return
            inorder(root.left)
            rem = k - root.val
            if rem in visited: self.res = True
            visited.add(root.val)
            inorder(root.right)
        
        inorder(root)
        return self.res