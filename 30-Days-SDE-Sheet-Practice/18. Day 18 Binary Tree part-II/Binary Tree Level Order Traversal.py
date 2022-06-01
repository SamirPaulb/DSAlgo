# https://leetcode.com/problems/binary-tree-level-order-traversal/

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        res = []
        if not root: return res
        q.append(root)
        
        while q:
            tmp = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                tmp.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(tmp)
            
        return res

# Time: O(N)
# Space: O(N)