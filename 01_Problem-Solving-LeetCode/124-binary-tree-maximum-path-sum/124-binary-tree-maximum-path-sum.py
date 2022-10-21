# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def solve(root):
            if not root: return 0
            l, r = 0, 0
            l = solve(root.left)
            r = solve(root.right)
            tmp = max(root.val + max(l, r), root.val)
            ans = max(root.val + l + r, tmp)
            self.res = max(self.res, ans)
            return tmp
        
        solve(root)
        return self.res