# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def solve(root, path):
            if not root: return ""
            if not root.left and not root.right:
                path += str(root.val)
                self.res += int(path)
            solve(root.left, path + str(root.val))
            solve(root.right, path + str(root.val))
        
        solve(root, "")
        return self.res