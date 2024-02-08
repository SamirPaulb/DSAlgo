# https://www.lintcode.com/problem/901
# https://www.youtube.com/watch?v=uIkji391mBI
# https://leetcode.com/problems/closest-binary-search-tree-value-ii/


import collections
class Solution:
    def closest_k_values(self, root: TreeNode, target: float, k: int) -> List[int]:
        q = collections.deque()
        def inorder_dfs(node):
            if not node: return 
            inorder_dfs(node.left)
            if len(q) < k:
                q.append(node.val)
            else:
                if abs(q[0] - target) > abs(node.val - target):
                    q.popleft()
                    q.append(node.val)
                else:
                    return 
            inorder_dfs(node.right)
        
        inorder_dfs(root)
        return list(q)

# Time: O(N)
