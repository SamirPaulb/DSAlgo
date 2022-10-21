# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def solve(root):
            if not root: return 0
            l = solve(root.left)
            r = solve(root.right)
            
            tmp = 1 + max(l, r)
            ans = max(tmp, 1 + l + r )
            self.res = max(self.res, ans)
            return tmp
        
        solve(root)
        return self.res - 1