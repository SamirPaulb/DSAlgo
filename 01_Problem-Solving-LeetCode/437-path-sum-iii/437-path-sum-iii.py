# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def solve(root, target):
            res = 0
            if not root: return 0
            if root.val == target:
                res += 1
            res += solve(root.left, target - root.val)
            res += solve(root.right, target - root.val)
            return res
        
        if not root: return 0
        return solve(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
    