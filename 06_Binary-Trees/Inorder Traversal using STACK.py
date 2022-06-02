# https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        cur = root
        while True:
            if cur != None:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right
            else:
                break
        return ans


