# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def solve(root, path):
            if not root: return
            if not root.left and not root.right:
                path += [root.val]
                if sum(path) == targetSum:
                    res.append(path)
            solve(root.left, path + [root.val])
            solve(root.right, path + [root.val])
        
        solve(root, [])
        return res