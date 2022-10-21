# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return None
        res = []
        q = [root]
        while q:
            n = len(q)
            tmp = []
            for i in range(n):
                node = q.pop(0)
                tmp.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(tmp)
        
        return res