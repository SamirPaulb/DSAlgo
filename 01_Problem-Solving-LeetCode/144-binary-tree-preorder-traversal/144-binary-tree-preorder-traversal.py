# Morris Preorder Traversal
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre and pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    res.append(cur.val)
                    pre.right = cur
                    cur = cur.left
                else:
                    cur = cur.right
        
        return res