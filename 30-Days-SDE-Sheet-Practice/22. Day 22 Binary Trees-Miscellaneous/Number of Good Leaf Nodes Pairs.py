# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

'''
Traverse from bottom to top (Postorder Traversal) and keep track of the distance of the 
leaf nodes to each node. Once those leaf nodes meet a Lowest Common Ancestor, 
we can immediately check whether they are good pairs.
'''

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0
        
        def dfs(node):
            nonlocal count
            
            if not node: return []
            if not node.left and not node.right: return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            count += sum(l + r <= distance for l in left for r in right)
            return [n + 1 for n in left + right if n + 1 < distance]
        
        dfs(root)
        return count
    
# Time: O(N)
# Space: O(N)
    
