# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return
        ans = root
        
        tmpRight = root.right
        root.right = None
        
        tmpLeft = root.left
        root.left = None
        
        self.flatten(tmpLeft)
        self.flatten(tmpRight)
        
        root.right = tmpLeft
        while root.right:
            root = root.right
        root.right = tmpRight
        
        return ans