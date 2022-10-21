# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.flag = False
        def solve(root, path):
            if not root: return
            if not root.left and not root.right:
                path += root.val
                if path == targetSum: 
                    self.flag = True
                    return
            solve(root.left, path+root.val)
            solve(root.right, path+root.val)
        
        solve(root, 0)
        return self.flag