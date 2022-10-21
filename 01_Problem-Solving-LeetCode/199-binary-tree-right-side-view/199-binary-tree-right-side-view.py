class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        res = []
        
        q = [root]
        while q:
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                if i == n-1:
                    res.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return res