# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0
        def solve(root):
            nonlocal count
            if not root: return []
            if not root.left and not root.right: return [1]
            left = solve(root.left)
            right = solve(root.right)
            for i in left:
                for j in right:
                    if i + j <= distance: count += 1
            arr = []
            for i in (left + right):
                if 1 + i < distance:
                    arr.append(1 + i)
            return arr
        solve(root)
        return count