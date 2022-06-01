# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        if not root: return res
        zigzag = True
        q = collections.deque()
        q.append(root)
        
        while q:
            n = len(q)
            nodesOfThisLevel = []
            
            for i in range(n):
                node = q.popleft()
                nodesOfThisLevel.append(node.val)
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                    
            if zigzag:
                res.append(nodesOfThisLevel)
                zigzag = False
            else:
                res.append(nodesOfThisLevel[::-1])
                zigzag = True
        
        return res
    
# Time: O(N)
# Space: O(N)
