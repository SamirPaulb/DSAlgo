# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        def solve(l, r):
            if not l and not r: return True
            elif not l or not r: return False
            return (l.val == r.val and
                    solve(l.left, r.right) and
                    solve(l.right, r.left))
        
        return solve(root.left, root.right)