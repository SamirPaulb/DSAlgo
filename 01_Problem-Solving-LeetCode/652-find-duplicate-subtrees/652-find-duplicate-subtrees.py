# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtreeDic = {}
        res = []
        
        def solve(root):
            if not root: return "#"
            l = solve(root.left)
            r = solve(root.right)
            key = l + "-" + r + "-" + str(root.val)
            if key not in subtreeDic: subtreeDic[key] = 1
            else: subtreeDic[key] += 1
            if subtreeDic[key] == 2: res.append(root)
            return key
        
        solve(root)
        return res