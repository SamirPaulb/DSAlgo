# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return 
        q = collections.deque()
        q.append(root)
        res = []
        flag = 1
        
        while q:
            n = len(q)
            arr = []
            for i in range(n):
                node = q.popleft()
                arr.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(arr) if flag == 1 else res.append(arr[::-1])
            flag *= -1
        
        return res