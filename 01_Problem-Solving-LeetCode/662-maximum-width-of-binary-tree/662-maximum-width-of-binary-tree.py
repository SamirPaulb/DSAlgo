class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root: return res
        q = collections.deque()
        q.append((root, 0))
        while q:
            distDiff = q[-1][1] - q[0][1] + 1
            res = max(res, distDiff)
            n = len(q)
            for i in range(n):
                node, dist = q.popleft()
                if node.left: q.append((node.left, 2*dist - 1))
                if node.right: q.append((node.right, 2*dist))
                    
        return res